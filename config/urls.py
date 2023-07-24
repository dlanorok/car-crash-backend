"""nesreca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.crashes.urls import router as crash_router
from api.cars.urls import router as car_router
from api.policy_holders.urls import router as policy_holder_router
from api.insurances.urls import router as insurance_router
from api.drivers.urls import router as driver_router
from api.circumstances.urls import router as circumstance_router
from api.files.urls import router as file_router
from api.common.urls import router as common_router
from api.sketches.urls import router as sketch_router
from api.questionnaires.urls import router as questionnaire_router

router = routers.DefaultRouter()
router.registry.extend(crash_router.registry)
router.registry.extend(car_router.registry)
router.registry.extend(policy_holder_router.registry)
router.registry.extend(insurance_router.registry)
router.registry.extend(driver_router.registry)
router.registry.extend(circumstance_router.registry)
router.registry.extend(file_router.registry)
router.registry.extend(common_router.registry)
router.registry.extend(sketch_router.registry)
router.registry.extend(questionnaire_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
