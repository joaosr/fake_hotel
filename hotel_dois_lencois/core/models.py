from django.db import models
from django.db.models import Q

class Reservation(models.Model):
    date_in = models.DateField('Date In', blank=False, null=False)
    date_out = models.DateField('Date Out', blank=False, null=False)
    guest_number = models.IntegerField('Number of guests', blank=False, null=False, default=1)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return "{0};{1}".format(self.date_in,self.date_out)

class Room(models.Model):
    OCCUPIED = 'Occupied'
    VACANT = 'Vacant'
    ROOM_STATUS = (
        (OCCUPIED, 'Occupied'),
        (VACANT, 'Vacant')
    )
    number = models.IntegerField('Number', blank=False, null=False)
    status = models.CharField('Status', max_length=20, choices=ROOM_STATUS)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return str(self.number)

    @staticmethod
    def find_vacant_room_for_period(date_from, date_to):
        occupiedRooms = OccupiedRoom.find_occupied_rooms_in_period(date_from, date_to)
        return Room.objects.exclude(id__in=occupiedRooms.values('room'))


class OccupiedRoom(models.Model):
    check_in = models.DateField('Check In', blank=False, null=False)
    check_out = models.DateField('Check Out', blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return str(self.room.number)

    @staticmethod
    def find_occupied_rooms_in_period(date_from, date_to):
        return OccupiedRoom.objects.filter(
            Q(check_in__lt=date_from, check_out__gt=date_from) |
            Q(check_in__lt=date_to, check_out__gt=date_to)
        )
