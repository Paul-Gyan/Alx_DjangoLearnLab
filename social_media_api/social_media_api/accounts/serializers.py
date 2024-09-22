from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    new_field = serializers.CharField()
 

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],    
        )
        return user

    class Meta: 
        model = Token
        fields ['key']

    def create(self, validated_data):
        token = Token.objects.create(user=validated_data['user'])
        return token