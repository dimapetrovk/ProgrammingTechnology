from rest_framework.response import Response
from rest_framework.views import APIView

from auto_base.serializers.car import CarSerializer
from ..models import Order
from ..serializers import OrderSerializer


class OrderAPIView(APIView):
    """
    CRUD for single order
    """

    def get(self, request, id, format=None):
        """
        Get order by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Order.objects.get(pk=id)
            serializer = OrderSerializer(item)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        """
        Update order by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Order.objects.get(pk=id)
        except Order.DoesNotExist:
            return Response(status=404)
        item.is_delivered = request.data['is_delivered']
        item.car.is_broken = request.data['car_is_broken']

        serializer = OrderSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()

        serializer = CarSerializer(item.car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        """
        Remove order by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Order.objects.get(pk=id)
        except Order.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)