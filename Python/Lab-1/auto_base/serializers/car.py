from rest_framework.serializers import ModelSerializer
from ..models import Car


class CarSerializer(ModelSerializer):
    """
    DRF serializer for Car model
    """
    class Meta:
        model = Car
        fields = '__all__'
