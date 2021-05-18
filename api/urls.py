from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
