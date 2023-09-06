from django.contrib import admin

# Register your models here.
from api.questionnaires.models import Questionnaire

admin.site.register(Questionnaire)
