from .models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

        def create(self, validated_data):
            model = self.Meta.model
            password = validated_data["password"]
            email = validated_data["email"]
            name = validated_data["name"]

            user = model.objects.create(email=email)
            user.set_password(password)
            user.save()

            return user
        
        def to_representation(self, instance):
            return{
                "id":instance.id,
                "name":instance.name,
                "email":instance.email
            }
            

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token_access', 'token_refresh']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        try:
            user = User.objects.get(email=email)
            if password == user.password:
                return {
                    'email': user.email,
                    'tokens_access': user.tokens_access(),
                    'tokens_refresh': user.tokens_refresh(),
                }
            else:
                raise serializers.ValidationError({'password': 'Incorrect password'})
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'User does not exist'})
        
        
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']