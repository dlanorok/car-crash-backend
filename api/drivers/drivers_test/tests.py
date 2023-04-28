import pytest
from rest_framework import status
from rest_framework.test import APIClient

from api.cars.cars_tests.factories import CarFactory
from api.cars.models import Car
from api.cars.serializers import CarSerializer
from api.crashes.models import Crash
from api.drivers.drivers_test.factories import DriverFactory
from api.drivers.models import Driver
from api.drivers.serializers import DriverSerializer

pytestmark = pytest.mark.django_db

@pytest.mark.django_db(transaction=True)
class TestClient:
    model = Driver
    client = APIClient()

    def test_create_driver(self):
        driver = DriverFactory.build()
        response = self.client.post("/api/v1/drivers/", DriverSerializer(driver).data, format='json')
        result = response.json()

        assert result['name'] == driver.name
        assert result['surname'] == driver.surname
        assert result['email'] == driver.email
        assert result['address'] == driver.address
        assert result['post_number'] == driver.post_number
        assert result['country_code'] == driver.country_code
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_drivers(self):
        DriverFactory.create_batch(5)
        response = self.client.get("/api/v1/drivers/", format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 5

    def test_update_driver(self):
        driver = DriverFactory.create()

        response = self.client.get(f'/api/v1/drivers/{driver.id}/', format='json')
        response_driver = DriverSerializer(response.json()).data
        assert response.status_code == status.HTTP_200_OK
        assert driver.name == response_driver.get('name')

        driver.name = 'newName'
        response = self.client.patch(f'/api/v1/drivers/{driver.id}/', DriverSerializer(driver).data, format='json')
        response_driver = DriverSerializer(response.json()).data

        assert response.status_code == status.HTTP_200_OK
        assert driver.name == response_driver.get('name')

    @pytest.mark.parametrize("field", ['name', 'surname', 'email', 'address', 'post_number', 'country_code'])
    def test_update_driver_by_parts(self, field):
        mock_driver = DriverFactory.build()
        driver = Driver()

        response = self.client.post("/api/v1/drivers/", DriverSerializer(driver).data, format='json')
        assert response.json().get('id') is not None

        setattr(driver, field, DriverSerializer(mock_driver).data[field])
        response = self.client.patch(f'/api/v1/drivers/{response.json().get("id")}/', DriverSerializer(driver).data, format='json')

        assert response.json().get(field) == getattr(mock_driver, field)
        assert Driver.objects.count() == 1

    def test_create_driver_under_car(self):
        car = CarFactory.create()

        assert Car.objects.count() == 1
        assert Crash.objects.count() == 1

        driver = DriverFactory.create()
        car.driver = driver

        response = self.client.patch(f'/api/v1/cars/{car.id}/', CarSerializer(car).data, format='json')
        result = response.json()

        assert result['driver'] == driver.id

    def test_add_car_to_driver(self):
        car = CarFactory.create()
        driver = DriverFactory.create()

        assert not hasattr(driver, 'car')

        driver.car = car
        response = self.client.patch(f'/api/v1/drivers/{driver.id}/', DriverSerializer(driver).data, format='json')
        result = response.json()

        assert result['car'] == car.id







