from django.test import TestCase
from .models import Dog, Breed, Job


class TestModels(TestCase):
    def test_dog_str_method_returns_name(self):
        dog = Dog.objects.create(name='Test Doggy', age=7, resided_since="2020-12-12")
        self.assertEqual(str(dog), 'Test Doggy')

    def test_breed_str_method_returns_breed_name(self):
        breed_name = Breed.objects.create(breed_name='Clifford the Red Dog')
        self.assertEqual(str(breed_name), 'Clifford the Red Dog')

    def test_job_str_method_returns_title(self):
        job = Job.objects.create(title='Canine Detective')
        self.assertEqual(str(job), 'Canine Detective')
