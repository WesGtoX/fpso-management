from rest_framework import viewsets, decorators, response, status

from equipment.models import Equipment
from equipment.serializers import EquipmentRetrieveSerializer
from vessel.models import Vessel
from vessel.serializers import VesselSerializer


class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = []

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'equipments':
            return EquipmentRetrieveSerializer

        return VesselSerializer

    @decorators.action(methods=['GET'], detail=True)
    def equipments(self, request, *args, **kwargs):
        vessel = self.get_object()
        equipments = Equipment.objects.filter(vessel=vessel, status=True)
        serializer = self.get_serializer(equipments, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
