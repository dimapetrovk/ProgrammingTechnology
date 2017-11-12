from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import DriverSerializer
from ..models import Driver


class DriverAPIView(APIView):
    """
    CRUD for single driver
    """
    def get(self, request, id, format=None):
        """
        Get driver by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Driver.objects.get(pk=id)
            serializer = DriverSerializer(item)
            return Response(serializer.data)
        except Driver.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        """
        Update driver by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Driver.objects.get(pk=id)
        except Driver.DoesNotExist:
            return Response(status=404)
        serializer = DriverSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        """
        Delete driver by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Driver.objects.get(pk=id)
        except Driver.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DriverAPIListView(APIView):

    def get(self, request, format=None):
        """
        Get Driver list
        :param request:
        :param format:
        :return:
        """
        items = Driver.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DriverSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """
        Create new Driver
        :param request:
        :param format:
        :return:
        """
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
