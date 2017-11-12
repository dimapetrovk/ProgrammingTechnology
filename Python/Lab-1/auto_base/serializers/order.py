from logging import Logger

logger = Logger('Serializer')

from rest_framework.serializers import ModelSerializer
from ..models import Order


class OrderSerializer(ModelSerializer):
    """
    General DRF serializer for Order model
    """

    class Meta:
        model = Order
        fields = '__all__'