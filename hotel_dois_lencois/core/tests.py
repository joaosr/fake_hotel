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
        self.assertTemplateUsed(self.response, 'index.html')


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

class OccupiedRoomModelTest(TestCase):
    def setUp(self):
        room = Room(
            number=1,
            status='Occupied'
        )
        reservation = Reservation(
            date_in='2019-10-01',
            date_out='2019-10-10'
        )
        reservation.save()
        room.save()

        self.obj = OccupiedRoom(
            check_in='2019-10-01',
            check_out='2019-10-15',
            room=room,
            reservation=reservation
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(OccupiedRoom.objects.exists())

    def test_created_at(self):
        """ OccupiedRoom must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('1', str(self.obj))


class TestReservationPost(TestCase):
    def setUp(self):
        data = dict(date_in='2019-10-01', date_out='2019-10-15', guests=4)
        self.resp = self.client.post('/', data, follow=True)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_post_content(self):
        content = b'{"nome": "Joao"}'
        self.assertEqual(self.resp.content, content)
