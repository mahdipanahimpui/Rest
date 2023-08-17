# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerilizer
from rest_framework.permissions import IsAuthenticated

# methods that are available
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     # send a dict
#     return Response({'name': 'mahdi'})


class Home(APIView):
    def get(self, request): 
        # get(self, request, name) getting params from url /mahdi, in path /<str:name>
        # get the query_params ?name=mahdi
        name = request.query_params['name']
        return Response({'name': f'your name: {name}'})
    
    def post(self, request):
        name = request.data['name'] # getting the data that is sent by post
        return Response({'name': f'your name: {name}'})




class Serializer(APIView):
    # to see view by perm send the authorization in headers
    # in headers:
    #       Authorization                      Token <token_value>
    permission_classes = [IsAuthenticated] # could use checking permissions in settings.py for all views

    def get(self, request):
        persons = Person.objects.all()
        # in here (instance): serializer is used to convert to json
        ser_data = PersonSerilizer(instance=persons, many=True)
        return Response(data=ser_data.data)
