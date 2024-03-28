from rest_framework import serializers
from authentication.models import User, ProfessionalCode
from django.contrib.auth import authenticate


class userSerializer(serializers.ModelSerializer):
   
  class Meta:
        model = User
        fields = "__all__"

# class profSignUpSerializer(serializers.Serializer):
#   first_name = serializers.CharField(max_length=50)
#   last_name = serializers.CharField(max_length="50")
#   surname = serializers.CharField(max_length="50")
#   email = serializers.EmailField()
#   password = serializers.CharField(max_leg)

class profCodeSerializer(serializers.ModelSerializer):
   class Meta:
      model = ProfessionalCode
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



