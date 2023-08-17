from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        # in here data is used to convert json that is posted by client to django model
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)  # like cleaned_data

            return Response(ser_data.data)
        return Response(ser_data.errors)
