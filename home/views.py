# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


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
