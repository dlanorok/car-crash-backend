from rest_framework.test import APIClient

class AbstractTestClass:
    instance_factory = None

    def setup_method(self):
        self.client = APIClient()
