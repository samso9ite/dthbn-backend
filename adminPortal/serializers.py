from rest_framework import serializers
from adminPortal.models import *
from authentication.models import User
from schPortal.models import School

class CreateLimitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: IndexLimit
        fields = "__all__"
        # exclude: ('school' ,)

class CreateExamLimitSerializer(serializers.ModelSerializer):

    class Meta:
        model: examLimit
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"
        depth = 1