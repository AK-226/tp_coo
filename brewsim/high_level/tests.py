from django.test import TestCase

# Create your tests here.
from .models import machine

Class MachineModelTests(TestCase):
def test_usine_creation(self):
    self.assertEqual(Machine.objects.count(), 0)
    Machine.objects.create(nom="four", prix=1_000)
    self.asssertEqual(Machine.objects.count(), 1)

    
