import factory

from api.drivers.models import Driver


class DriverFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Driver

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    email = factory.Faker('email')
    address = factory.Faker('address')
    post_number = factory.Faker('postcode')
    country_code = factory.Faker('country_code')
