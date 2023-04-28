import pytest
from rest_framework import status
from rest_framework.test import APIClient

from api.crashes.crashes_tests.factories import CrashFactory
from api.crashes.models import Crash
from api.crashes.serializers import CrashSerializer

pytestmark = pytest.mark.django_db

class BaseCrashTest:
    factory = CrashFactory
    serializer = CrashSerializer
    model = Crash


@pytest.mark.django_db(transaction=True)
class TestCrashAPIClient(BaseCrashTest):
    client = APIClient()

    def test_create_crash(self):
        response = self.client.post("/api/v1/crashes/", {}, format='json')
        result = response.json()

        assert result['closed'] is False
        assert result['session_id'] is not None
        assert response.status_code == status.HTTP_201_CREATED


    def test_update_crash(self):
        # create crash
        response = self.client.post("/api/v1/crashes/", {}, format='json')
        result = response.json()

        result['closed'] = True
        response = self.client.patch(f'/api/v1/crashes/{result["id"]}/', result, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'closed' in response.json()
        assert 'session_id' in response.json()

    def test_delete_crash(self):
        crash = self.factory.create()

        response = self.client.delete(f'/api/v1/crashes/{crash.id}/')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


class TestCrashes(BaseCrashTest):
    def test_delete_session_after_save(self):
        crash = self.factory.build()
        crash.closed = False
        crash.save()

        crash.closed = True
        crash.save()
        assert crash.session_id is None
