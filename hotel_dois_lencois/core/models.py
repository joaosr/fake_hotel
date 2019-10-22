from django.db import models

class Reservation(models.Model):
    date_in = models.DateField('Date In', blank=True, null=True)
    date_out = models.DateField('Date Out', blank=True, null=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
