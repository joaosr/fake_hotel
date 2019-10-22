from django.test import TestCase
from hotel_dois_lencois.core.models import Reservation

# Create your tests here.
class TestReservationModel(TestCase):

    def test_simple_case(self):
        reservation = Reservation(
                        date_in='2010-05-15',
                        date_out='2010-05-15')

        reservation.save()
        self.assertTrue(Reservation.objects.exists())
