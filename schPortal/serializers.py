from rest_framework import serializers
from schPortal.models import *

class schUpdateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(required=False)
    region = serializers.CharField(required=False)
   
    class Meta:
        model = School
        fields = ('postal_number', 'phone_number', 'region', 'hod_name', 'hod_phone', 'hod_email','address', 'state', 'sch_logo',)