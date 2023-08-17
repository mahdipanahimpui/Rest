from rest_framework import serializers
from .models import Question, Answer

# modelname + Serialiazer
class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    age = serializers.IntegerField()
    name = serializers.CharField()





class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    # method field to send other fields
    #   mehtod name: get_<field_name>
    def get_answers(self, obj): # obj is the Question instance
        reslut = obj.answers.all()
        return AnswerSerializer(instance=reslut, many=True).data



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


