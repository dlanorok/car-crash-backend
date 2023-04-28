import factory

from api.crashes.models import Crash

class CrashFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Crash

    created_at = factory.Faker('first_name')
    closed = factory.Faker('pybool')
    session_id = factory.Faker('pystr', min_chars=5)
