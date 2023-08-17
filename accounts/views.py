from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


class UserRegisterView(APIView):
    def post(self, request):
        # in here data is used to convert json that is posted by client to django model
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)  # like cleaned_data

            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST) # adding custum status code, status=1000, status=status.HTTP_200_CREATED




# viewsets used for LIGHT CODING not COMPLEX
### note: has_object_permissions (object-level perm) not working in viewsets
# config the urls.py by routers
class UserViewSet(viewsets.ViewSet):  # about def action see router docs
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()


    def list(self, request): # read all objects
        sre_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=sre_data.data)



    def create(self, request): # to create an object
        ser_data = UserSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()  # like cleaned_data
            return Response(ser_data.data)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST) 



    def retrieve(self, request, pk=None): # read object
        user = get_object_or_404(self.queryset, pk=pk)
        sre_data = UserSerializer(instance=user)

        return Response(data=sre_data.data)



    def update(self, request, pk=None): # update object, if object is not exists, create that
        pass

    

    def partial_update(self, request, pk=None): # partial update
        # active with PATCH
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'message': 'owner pemission denied'})
        sre_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if sre_data.is_valid():
            sre_data.save()
            return Response(data=sre_data.data)
        return Response(data=sre_data.errors)




    def destroy(self, request, pk=None): # delere object
        user = get_object_or_404(self.queryset, pk=pk)
        username = user.username
        user.is_active = False
        user.save()
        return Response({'message:' f'{username} is deactivated'})



class TestUserPagination(APIView):

    def get(self, request):

        queryset = User.objects.all()
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 1)
        paginator = Paginator(queryset, page_size)
        sre_data = UserSerializer(instance=paginator.page(page_number), many=True)
        return Response(data=sre_data.data)