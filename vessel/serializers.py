from rest_framework import serializers
from vessel.models import Vessel


class VesselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vessel
        fields = ('id', 'code')
