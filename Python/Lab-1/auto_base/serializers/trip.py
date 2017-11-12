from logging import Logger

logger = Logger('Serializer')

from rest_framework.serializers import ModelSerializer
from ..models import Trip


class TripSerializer(ModelSerializer):
    """
    General DRF serializer for Trip model
    """

    class Meta:
        model = Trip
        fields = '__all__'
