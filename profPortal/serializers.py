from rest_framework import serializers
from profPortal.models import *

class professionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professional
        fields= "__all__"
        depth = 1

class licenseReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseReceipt
        fields = "__all__"
        depth = 1