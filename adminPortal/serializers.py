from rest_framework import serializers
from adminPortal.models import *

class CreateLimitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: IndexLimit
        fields = "__all__"
        # exclude: ('school' ,)

class CreateExamLimitSerializer(serializers.ModelSerializer):

    class Meta:
        model: examLimit
        fields = "__all__"