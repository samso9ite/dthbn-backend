from rest_framework import serializers
from adminPortal.models import *
from authentication.models import User
from schPortal.models import School

class CreateLimitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IndexLimit
        fields = "__all__"

class CreateExamLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = examLimit
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

class indexStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = closeIndexing
        fields = "__all__"

class examStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = closeExamRegistration
        fields = "__all__"

class declineIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexing
        fields = ('comment', 'approved', 'unapproved',)

class declineExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamRegistration
        fields = ('comment', 'approved', 'unapproved',)

class licenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = licenseModel
        fields = "__all__"
        depth = 1

class createLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = licenseModel
        fields = ("prof", "renewal_date", "expiry_date", "status", "certificate")
     