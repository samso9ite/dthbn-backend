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

# Create your views here
class UpdateProfileView(UpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = professionalSerializer 
    permission_classes = [IsAuthenticated]  
    lookup_field = 'id'

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
    print(user)
    if user.is_professional:
        print(user)
        if user.is_active:
            print("I'm here now")
            license = licenseModel.objects.filter(prof_id=user.id)
            serialized_license = licenseSerializer(license, many=True).data
            serialized_user = userSerializer(user).data
            license_count = license.count()
            print(license_count)
            context = {
                'license':serialized_license,
                'license_count': license_count,
                'user':serialized_user
            }
            return Response({"data": context, "message": "Request Successfull"}, status=status.HTTP_200_OK)
    return Response({"message": "User not Professional"}, status=status.HTTP_404_NOT_FOUND)