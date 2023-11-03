from rest_framework import serializers
from schPortal.models import *

class schUpdateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(required=False)
    region = serializers.CharField(required=False)
   
    class Meta:
        model = School
        fields = ('postal_number', 'phone_number', 'region', 'hod_name', 'hod_phone', 'hod_email','address', 'state', 'sch_logo',)

class indexingSerializer(serializers.ModelSerializer):
    submitted = serializers.BooleanField(default=False, allow_null = True)
    approved = serializers.BooleanField(default=False, allow_null = True)
    comment = serializers.CharField(allow_null=True)
    verified = serializers.BooleanField(allow_null=True, default=False)
    closed = serializers.BooleanField(allow_null=True, default=False)
    class Meta:
        model = Indexing
        fields = ("__all__")

class examSerializer(serializers.ModelSerializer):
    submitted = serializers.BooleanField(default=False, allow_null = True)
    approved = serializers.BooleanField(default=False, allow_null = True)
    comment = serializers.CharField(allow_null=True)
    verified = serializers.BooleanField(allow_null=True, default=False)
    class Meta:
        model = ExamRegistration
        fields = ("__all__")