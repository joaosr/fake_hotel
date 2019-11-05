from django.db import models

class Reservation(models.Model):
    date_in = models.DateField('Date In', blank=False, null=False)
    date_out = models.DateField('Date Out', blank=False, null=False)
    guest_number = models.IntegerField('Number of guests', blank=False, null=False, default=1)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return "{0};{1}".format(self.date_in,self.date_out)

class RoomType(models.Model):
    description = models.TextField('Description', blank=True, null=True)
    max_capacity = models.IntegerField('Max Capacity', blank=False, null=False, default=1)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return self.description

class Room(models.Model):
    OCCUPIED = 'Occupied'
    VACANT = 'Vacant'
    ROOM_STATUS = (
        (OCCUPIED, 'Occupied'),
        (VACANT, 'Vacant')
    )
    number = models.IntegerField('Number', blank=False, null=False)
    status = models.CharField('Status', max_length=20, choices=ROOM_STATUS)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return str(self.number)


class OccupiedRoom(models.Model):
    check_in = models.DateField('Check In', blank=False, null=False)
    check_out = models.DateField('Check Out', blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return str(self.room.number)
