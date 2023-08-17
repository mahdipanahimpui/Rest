from rest_framework import serializers
from django.contrib.auth.models import User


# is a third way to validate
def check_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin word must not be at email')


# serializer is used to convert to json and reverse to django model
# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True, validators=[check_email])
#     password = serializers.CharField(required=True)
#     confirm_password = serializers.CharField(required=True)


#### use model serializer ####

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        # exclude = ('email', ) # all exclude the username, dont use fields again
        # fields = '__all__' # to get all fields
        fields = ('username', 'email', 'password', 'confirm_password')

        # to make readonly the password
        extra_kwargs = {
            'password' : {'write_only':True}, # wont be shown in the return Response(ser_data.data) >> for confirm_password ABOVE
            'email': {'validators': (check_email,)}
        }

    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    # valus is the field that is sent
    ## field level validation
    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be `admin`')
        return value

        
    # data is required
    ## object level validation
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password must match')
        return data
    



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'