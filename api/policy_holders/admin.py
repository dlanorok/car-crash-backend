from django.contrib import admin

# Register your models here.
from api.policy_holders.models import PolicyHolder

admin.site.register(PolicyHolder)
