from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from users.viewsets import UserViewSet
from vessel.viewsets import VesselViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('vessel', VesselViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
