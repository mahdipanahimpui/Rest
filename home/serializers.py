from rest_framework import serializers
from .models import Question, Answer
from .custom_relational_fields import UserEmailNameRelationalField

# modelname + Serialiazer
class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    age = serializers.IntegerField()
    name = serializers.CharField()





class QuestionSerializer(serializers.ModelSerializer):
    # answers = serializers.SerializerMethodField()
    # user field is exists in Question model as a relation, to customize the presentation usse serializer-relation
    # user = serializers.StringRelatedField(read_only=True) # return the __str__
    # user = serializers.PrimaryKeyRelatedField(read_only=True) # the default thread
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email') # to use other field

    # for custom serializer_relation use custom relational fields 
    user = UserEmailNameRelationalField(read_only=True)

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


