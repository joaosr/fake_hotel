from django.db import models

class Reservation(models.Model):
    date_in = models.DateField('Date In', blank=False, null=False)
    date_out = models.DateField('Date Out', blank=False, null=False)
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

class OccupiedRoom(models.Model):
    check_in = models.DateField('Check In', blank=False, null=False)
    check_out = models.DateField('Check Out', blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return str(self.room.number)
