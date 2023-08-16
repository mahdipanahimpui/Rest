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
        return Response({'name': 'mahdi'})