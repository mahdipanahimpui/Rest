from rest_framework import serializers


# is a third way to validate
def check_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin word must not be at email')

# serializer is used to convert to json and reverse to django model
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[check_email])
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

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