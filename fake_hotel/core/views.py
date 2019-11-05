from django.shortcuts import render
from django.db.models import Q, Count
from fake_hotel.core.forms import ReservationForm
from fake_hotel.core.models import Room, Reservation, OccupiedRoom

# Create your views here.
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            context['reservation'] = Reservation(
             date_in=form.cleaned_data['date_in'],
             date_out=form.cleaned_data['date_out'],
             guest_number=form.cleaned_data['guest_number']
            )
            date_from = form.cleaned_data['date_in']
            date_to = form.cleaned_data['date_out']
            context['rooms'] = find_vacant_room_for_period(date_from, date_to)

        return render(request, 'reservation.html', context)
    else:
        context = {'form': ReservationForm()}
        return render(request, 'reservation.html', context)


def find_vacant_room_for_period(date_from, date_to):
    occupiedRooms = find_occupied_rooms_in_period(date_from, date_to)
    rooms = Room.objects.exclude(id__in=occupiedRooms.values('room'))
    return group_by_room_type(rooms)

def find_occupied_rooms_in_period(date_from, date_to):
    return OccupiedRoom.objects.filter(
        Q(check_in__lt=date_from, check_out__gt=date_from) |
        Q(check_in__lt=date_to, check_out__gt=date_to)
    )

def group_by_room_type(rooms):
    return rooms.values('room_type__description', 'room_type__max_capacity').annotate(room_available=Count('id'))
