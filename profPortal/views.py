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