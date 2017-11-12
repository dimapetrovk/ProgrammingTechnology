from rest_framework.serializers import ModelSerializer
from ..models import Driver


class DriverSerializer(ModelSerializer):
    """
    DRF serializer for Driver model
    """

    class Meta:
        model = Driver
        fields = '__all__'
