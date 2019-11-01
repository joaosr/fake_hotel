from datetime import datetime
from django.test import TestCase
from hotel_dois_lencois.core.models import Reservation, Room, OccupiedRoom

# Create your tests here.
class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'reservation.html')


class ReservationModelTest(TestCase):
    def setUp(self):
        self.obj = Reservation(
            date_in='2019-10-01',
            date_out='2019-10-10'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Reservation.objects.exists())

    def test_created_at(self):
        """ Room must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('2019-10-01;2019-10-10', str(self.obj))


class RoomModelTest(TestCase):
    def setUp(self):
        self.obj = Room(
            number=1,
            status='Occupied'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Room.objects.exists())

    def test_created_at(self):
        """ Reservation must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('1', str(self.obj))

    def test_find_vacant_room_for_period(self):
        reservation = Reservation(
            date_in='2019-10-01',
            date_out='2019-10-15'
        )
        occupiedRoom = OccupiedRoom(
            check_in=reservation.date_in,
            check_out=reservation.date_out,
            room=self.obj,
            reservation=reservation
        )

        rooms = Room.find_vacant_room_for_period(
            '2020-01-01',
            '2020-01-15')

        self.assertEqual(rooms.count(), 1)


class OccupiedRoomModelTest(TestCase):
    def setUp(self):
        self.room = Room(
            number=1,
            status='Occupied'
        )
        self.reservation = Reservation(
            date_in='2019-10-05',
            date_out='2019-10-10'
        )
        self.reservation.save()
        self.room.save()

        self.obj = OccupiedRoom(
            check_in='2019-10-01',
            check_out='2019-10-15',
            room=self.room,
            reservation=self.reservation
        )
        self.obj = OccupiedRoom(
            check_in='2019-10-01',
            check_out='2019-10-15',
            room=self.room,
            reservation=self.reservation
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(OccupiedRoom.objects.exists())

    def test_created_at(self):
        """ OccupiedRoom must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('1', str(self.obj))

    def test_occupied_rooms_in_period(self):
        occupiedRooms = OccupiedRoom.find_occupied_rooms_in_period(
            self.reservation.date_in,
            self.reservation.date_out)

        self.assertEqual(occupiedRooms.first().room, self.room)

    def test_no_occupied_rooms_in_period(self):
        occupiedRooms = OccupiedRoom.find_occupied_rooms_in_period(
            '2020-01-01',
            '2020-01-15')

        self.assertEqual(occupiedRooms.count(), 0)


class TestReservationPost(TestCase):
    def setUp(self):
        data = dict(date_in='2019-10-01', date_out='2019-10-15', guests=4)
        self.resp = self.client.post('/', data, follow=True)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
