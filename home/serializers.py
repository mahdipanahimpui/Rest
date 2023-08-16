from rest_framework import serializers


# modelname + Serialiazer
class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    age = serializers.IntegerField()
    name = serializers.CharField()