from django import forms
import datetime

class ReservationForm(forms.Form):
    date_in = forms.DateField(label='Check-in', initial=datetime.date.today)
    date_out = forms.DateField(label='Check-out', initial=datetime.date.today)
