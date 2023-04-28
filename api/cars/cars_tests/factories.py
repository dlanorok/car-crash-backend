import factory

from api.cars.models import Car
from api.crashes.crashes_tests.factories import CrashFactory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    name = factory.Faker('first_name')
    registration_plate = factory.Faker('pystr', min_chars=5, max_chars=8)
    crash = factory.SubFactory(CrashFactory)
