import factory

from api.policy_holders.models import PolicyHolder


class PolicyHolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PolicyHolder

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    email = factory.Faker('email')
    address = factory.Faker('address')
    post_number = factory.Faker('postcode')
    country_code = factory.Faker('country_code')
