from rest_framework import serializers
from authentication.models import User

class userSerializer(serializers.ModelSerializer):
   
  class Meta:
        model = User
        fields = "__all__"

class loginSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ['email', 'password',]

class accountActivationSerializer(serializers.Serializer):
  token = serializers.CharField(max_length=100)
  uidb = serializers.CharField(max_length=200)

class passwordResetSerializer(serializers.Serializer):
  new_password = serializers.CharField(write_only=True)
  confirm_password = serializers.CharField(write_only=True)

class forgotPasswordSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=100)
