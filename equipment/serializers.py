from rest_framework import serializers
from equipment.models import Equipment


class EquipmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id', 'name', 'code', 'location', 'status', 'vessel')
        read_only_fields = ('status',)


class EquipmentRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id', 'name', 'code', 'location', 'status')
