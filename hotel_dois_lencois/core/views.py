from django.shortcuts import render
from hotel_dois_lencois.core.forms import ReservationForm
from django.core import serializers
from hotel_dois_lencois.core.models import Room, Reservation


# Create your views here.
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation(
             date_in=form.cleaned_data['date_in'],
             date_out=form.cleaned_data['date_out'],
             guest_number=form.cleaned_data['guest_number']
            )
            date_from = form.cleaned_data['date_in']
            date_to = form.cleaned_data['date_out']
            rooms = Room.find_vacant_room_for_period(date_from, date_to)
            rooms_serialized = serializers.serialize('json', rooms)

            context = {'rooms': rooms_serialized, 'reservation': reservation}
            return render(request, 'reservation.html', context)
        else:
            return render(request, 'reservation.html', {'form': form})
    else:
        context = {'form': ReservationForm()}
        return render(request, 'reservation.html', context)
