from django.shortcuts import render
from django.views.generic import TemplateView , CreateView, UpdateView
from profPortal.forms import  ProfAccntForm
from profPortal.models import Professional
from adminPortal.models import licenseModel
from adminPortal.serializers import licenseSerializer
from django.urls import reverse_lazy
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import userSerializer
from authentication.models import User
from django.shortcuts import get_object_or_404


# Create your views here
class UpdateProfileView(UpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = professionalSerializer 
    permission_classes = [IsAuthenticated]  
    lookup_field = 'profuser_id'

class AddProfessionalView(CreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = professionalSerializer

class RetrieveProfView(RetrieveAPIView):
    queryset = Professional.objects.all()
    serializer_class = professionalSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'profuser'

class ListLicenseView(ListAPIView):
    queryset = licenseModel.objects.all()
    serializer_class = licenseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profDashboard(request):
    user=request.user
    if user.is_professional:
        if user.is_active:
            license = licenseModel.objects.filter(prof_id=user.id)
            serialized_license = licenseSerializer(license, many=True).data
            serialized_user = userSerializer(user).data
            license_count = license.count()
            context = {
                'license':serialized_license,
                'license_count': license_count,
                'user':serialized_user
            }
            return Response({"data": context, "message": "Request Successfull"}, status=status.HTTP_200_OK)
    return Response({"message": "User not Professional"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def verifyLicense(request, license_id, programme):
    codeVar = programme+license_id
    user = get_object_or_404(User, code=codeVar)
    license = licenseModel.objects.filter(prof_id=user.id).order_by('-created_date').first()
    profDetails = Professional.objects.filter(profuser_id=user.id)
    details = professionalSerializer(profDetails, many=True).data
    license_data = licenseSerializer(license).data
    context = {
        "license": license_data,
        "profDetails": details
    }
    return Response({"data": context, "message": "License Retrieved Successfully"}, status=status.HTTP_200_OK)

class UpdateLicenseReceiptView(UpdateAPIView):
    queryset = LicenseReceipt.objects.all()
    serializer_class = licenseReceiptSerializer 
    permission_classes = [IsAuthenticated]  
    lookup_field = 'id'

class AddLicenseReceiptView(CreateAPIView):
    queryset = LicenseReceipt.objects.all()
    serializer_class = licenseReceiptSerializer

class ListReceiptView(ListAPIView):
    serializer_class = licenseReceiptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # Get the authenticated user
        return LicenseReceipt.objects.filter(profuser=user)