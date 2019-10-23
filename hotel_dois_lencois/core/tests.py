from django.test import TestCase
from hotel_dois_lencois.core.models import Reservation

# Create your tests here.
class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')


class TestReservationModel(TestCase):

    def test_simple_case(self):
        reservation = Reservation(
        date_in='2010-05-15',
        date_out='2010-05-15')

        reservation.save()
        self.assertTrue(Reservation.objects.exists())
