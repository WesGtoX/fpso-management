from rest_framework import viewsets, status, response, decorators

from equipment.models import Equipment
from equipment.serializers import (
    EquipmentCreateSerializer,
    EquipmentRetrieveSerializer,
)


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permission_classes = []

    def get_serializer_class(self):
        action_list = ['create', 'update', 'partial_update']

        if hasattr(self, 'action') and self.action in action_list:
            return EquipmentCreateSerializer

        return EquipmentRetrieveSerializer

    @decorators.action(methods=['POST'], detail=False)
    def status_inactive(self, request, *args, **kwargs):
        """
        Setting an equipment’s status to inactive.
        """
        codes = dict(request.data)
        codes_list = codes.get('codes', [])

        if len(codes_list) == 0:
            error = dict(status=400, error={'message': 'One or more equipment code must be inputted.'})
            return response.Response(error, status=status.HTTP_400_BAD_REQUEST)

        equipments = Equipment.objects.filter(code__in=codes_list)

        if equipments.count() == 0:
            error = dict(status=404, error={'message': 'No equipment code found.'})
            return response.Response(error, status=status.HTTP_404_NOT_FOUND)

        for equipment in equipments:
            equipment.status = False

        Equipment.objects.bulk_update(objs=equipments, fields=['status'])

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(equipments, context=self.get_serializer_context(), many=True)
        return response.Response(serializer.data)
