from django import forms
import datetime
from django.forms.widgets import SplitDateTimeWidget

class DateInput(forms.DateInput):
    format_key = 'DATE_INPUT_FORMATS'
    input_type = 'date'

class ReservationForm(forms.Form):
    date_in = forms.DateField(label='Check-in', initial=datetime.date.today, widget=DateInput)
    date_out = forms.DateField(label='Check-out', initial=datetime.date.today, widget=DateInput)
    guests = forms.IntegerField(label='Guests', initial=0, min_value=0, max_value=7)
