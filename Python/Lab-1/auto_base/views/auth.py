from logging import Logger
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UserSerializer
from rest_framework.permissions import AllowAny

logger = Logger('Views')

class RegistrationAPIView(APIView):
    """
    Handle user authorization
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        logger.info('Data is not valid')
        return Response(serializer.errors, status=400)