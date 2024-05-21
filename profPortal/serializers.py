from rest_framework import serializers
from profPortal.models import Professional

class professionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professional
        fields= "__all__"
        depth = 1
