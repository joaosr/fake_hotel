from django.shortcuts import render
from hotel_dois_lencois.core.forms import ReservationForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        print('oi')
    else:
    	context = {'form': ReservationForm()}
    	return render(request, 'index.html', context)
