from rest_framework import serializers
from profPortal.models import *

class professionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professional
        fields= "__all__"
        depth = 1

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptModel
        fields = "__all__"
        # depth = 1
        