# from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerilizer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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








class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
        


    def post(self, request):
        sre_data = QuestionSerializer(data=request.data)
        if sre_data.is_valid():
            sre_data.save() # save() is availabel because of serializersModel
            return Response(sre_data.data, status=status.HTTP_201_CREATED)
        return Response(sre_data.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        sre_data = QuestionSerializer(instance=question, data=request.data, partial=True) # partial becaouse of update a part of obj not all
        if sre_data.is_valid():
            sre_data.save()
            return Response(sre_data.data, status=status.HTTP_200_OK) 
        return Response(sre_data.errors, status=status_HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        id = question.id
        question.delete()
        return Response({'message:': f'question with id {id}'}, status=status.HTTP_200_OK)


