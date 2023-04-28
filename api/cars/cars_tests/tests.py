import pytest
from rest_framework import status
from rest_framework.test import APIClient

from api.cars.cars_tests.factories import CarFactory
from api.cars.models import Car
from api.cars.serializers import CarSerializer
from api.crashes.crashes_tests.factories import CrashFactory
from api.crashes.models import Crash

pytestmark = pytest.mark.django_db

@pytest.mark.django_db(transaction=True)
class TestCarClient:
    model = Car
    client = APIClient()
    factory = CarFactory
    serializer = CarSerializer

    def setup_method(self):
        self.crash = CrashFactory.create()

    @pytest.mark.parametrize("num_cars", list(range(1, 5)))
    def test_create_car(self, num_cars):
        for i in range(num_cars):
            car = self.factory.build()
            car.crash = self.crash
            response = self.client.post("/api/v1/cars/", self.serializer(car).data, format='json')
            result = response.json()

            assert result['name'] == car.name
            assert result['registration_plate'] == car.registration_plate
            assert result['crash'] == self.crash.id
            assert result['creator'] is not None
            assert Crash.objects.get(id=result['crash']).session_id == self.crash.session_id
            assert response.status_code == status.HTTP_201_CREATED

        assert self.model.objects.count() == num_cars





