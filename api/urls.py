from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from users.viewsets import UserViewSet
from vessel.viewsets import VesselViewSet
from equipment.viewsets import EquipmentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('vessel', VesselViewSet)
router.register('equipment', EquipmentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
