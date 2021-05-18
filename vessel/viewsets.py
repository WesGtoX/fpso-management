from rest_framework import viewsets

from vessel.models import Vessel
from vessel.serializers import VesselSerializer


class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = []
