# from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerilizer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from . permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

# methods that are available
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     # send a dict
#     return Response({'name': 'mahdi'})


class Home(APIView):
    permission_classes = [AllowAny,]
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





class QuestionListView(APIView):
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_scope = 'question_throttle'

    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
        



class QuestionCreateView(APIView):
    """
        note: this view create question
    """
    serializer_class = QuestionSerializer

    def post(self, request):
        sre_data = QuestionSerializer(data=request.data)
        if sre_data.is_valid():
            sre_data.save() # save() is availabel because of serializersModel
            return Response(sre_data.data, status=status.HTTP_201_CREATED)
        return Response(sre_data.errors, status=status.HTTP_400_BAD_REQUEST)
    



class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly] # athentication needs token in header, if not exsit create by url

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        self.check_object_permissions(request, question) # to force the instance-level to check
        sre_data = QuestionSerializer(instance=question, data=request.data, partial=True) # partial becaouse of update a part of obj not all
        if sre_data.is_valid():
            sre_data.save()
            return Response(sre_data.data, status=status.HTTP_200_OK) 
        return Response(sre_data.errors, status=status.HTTP_400_BAD_REQUEST)



class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly] # isAuthenticated is checked in IsOwnwerOrReadOnly as a view-level perm
    
    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        self.check_object_permissions(request, question) # to force the instance-level to check
        id = question.id
        question.delete()
        return Response({'message:': f'question with id {id}'}, status=status.HTTP_200_OK)


