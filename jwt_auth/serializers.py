from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','email','password')


    def validate_user(self,data):


        if data.email  or data.username is None or data.password.length < 8:
            raise serializers.ValidationError("email or username is required")
        
        return data
