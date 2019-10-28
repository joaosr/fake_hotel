from django.shortcuts import render
from hotel_dois_lencois.core.forms import ReservationForm
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            return JsonResponse({'nome': 'Joao'})
        else:
            return render(request, 'index.html', {'form': form})
    else:
        context = {'form': ReservationForm()}
        return render(request, 'index.html', context)
