import pytest
from rest_framework import status
from rest_framework.test import APIClient

from api.cars.cars_tests.factories import CarFactory
from api.cars.models import Car
from api.cars.serializers import CarSerializer
from api.crashes.models import Crash
from api.policy_holders.policy_holders_test.factories import PolicyHolderFactory
from api.policy_holders.models import PolicyHolder
from api.policy_holders.serializers import PolicyHolderSerializer

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(transaction=True)
class TestClient:
    model = PolicyHolder
    client = APIClient()

    def test_create_policy_holder(self):
        policy_holder = PolicyHolderFactory.build()
        response = self.client.post("/api/v1/policy_holders/", PolicyHolderSerializer(policy_holder).data, format='json')
        result = response.json()

        assert result['name'] == policy_holder.name
        assert result['surname'] == policy_holder.surname
        assert result['email'] == policy_holder.email
        assert result['address'] == policy_holder.address
        assert result['post_number'] == policy_holder.post_number
        assert result['country_code'] == policy_holder.country_code
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_policy_holders(self):
        PolicyHolderFactory.create_batch(5)
        response = self.client.get("/api/v1/policy_holders/", format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 5

    def test_update_policy_holder(self):
        policy_holder = PolicyHolderFactory.create()

        response = self.client.get(f'/api/v1/policy_holders/{policy_holder.id}/', format='json')
        response_policy_holder = PolicyHolderSerializer(response.json()).data
        assert response.status_code == status.HTTP_200_OK
        assert policy_holder.name == response_policy_holder.get('name')

        policy_holder.name = 'newName'
        response = self.client.patch(f'/api/v1/policy_holders/{policy_holder.id}/', PolicyHolderSerializer(policy_holder).data, format='json')
        response_policy_holder = PolicyHolderSerializer(response.json()).data

        assert response.status_code == status.HTTP_200_OK
        assert policy_holder.name == response_policy_holder.get('name')

    @pytest.mark.parametrize("field", ['name', 'surname', 'email', 'address', 'post_number', 'country_code'])
    def test_update_policy_holder_by_parts(self, field):
        mock_policy_holder = PolicyHolderFactory.build()
        policy_holder = PolicyHolder()

        response = self.client.post("/api/v1/policy_holders/", PolicyHolderSerializer(policy_holder).data, format='json')
        assert response.json().get('id') is not None

        setattr(policy_holder, field, PolicyHolderSerializer(mock_policy_holder).data[field])
        response = self.client.patch(f'/api/v1/policy_holders/{response.json().get("id")}/', PolicyHolderSerializer(policy_holder).data, format='json')

        assert response.json().get(field) == getattr(mock_policy_holder, field)
        assert PolicyHolder.objects.count() == 1

    def test_create_policy_holder_under_car(self):
        car = CarFactory.create()

        assert Car.objects.count() == 1
        assert Crash.objects.count() == 1

        policy_holder = PolicyHolderFactory.create()
        car.policy_holder = policy_holder

        response = self.client.patch(f'/api/v1/cars/{car.id}/', CarSerializer(car).data, format='json')
        result = response.json()

        assert result['policy_holder'] == policy_holder.id

    def test_add_car_to_policy_holder(self):
        car = CarFactory.create()
        policy_holder = PolicyHolderFactory.create()

        assert not hasattr(policy_holder, 'car')

        policy_holder.car = car
        response = self.client.patch(f'/api/v1/policy_holders/{policy_holder.id}/', PolicyHolderSerializer(policy_holder).data, format='json')
        result = response.json()

        assert result['car'] == car.id







