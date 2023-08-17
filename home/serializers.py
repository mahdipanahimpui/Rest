from rest_framework import serializers
from .models import Question, Answer

# modelname + Serialiazer
class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    age = serializers.IntegerField()
    name = serializers.CharField()





class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


