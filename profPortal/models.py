from django.db import models
from authentication.models import User

# Create your models here.

class Professional(models.Model):
    profuser = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='profs')
    profile_image = models.ImageField(upload_to='images/professional/prof_profile_img', null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    postal_address = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    residential_country = models.CharField(max_length=100,  blank=True, null=True)
    residential_state = models.CharField(max_length=100,  blank=True, null=True)
    residential_lga = models.CharField(max_length=100, blank=True, null=True)
    residential_address = models.CharField(max_length=200, blank= True, null=True)
    marital_status = models.CharField(max_length=200, blank=True, null=True)
    maiden_name = models.CharField(max_length=200, blank=True, null=True)
    state_of_origin = models.CharField(max_length=100,  blank=True, null=True)
    lga_state = models.CharField(max_length=100, blank=True, null=True) 
    senatorial_district = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.CharField(max_length=30, blank=True, null=True)
    state_of_birth = models.CharField(max_length=100, blank=True, null=True)
    lga_of_birth = models.CharField(max_length=100, blank=True, null=True)
    qualification1 = models.CharField(max_length=200, blank=True, null=True)     
    qualification2 = models.CharField(max_length=200, blank=True, null=True)     
    qualification3 = models.CharField(max_length=200, blank=True, null=True) 
    qualification4 = models.CharField(max_length=200, blank=True, null=True) 
    institution_1 = models.CharField(max_length=200, blank=True, null=True) 
    institution_2 = models.CharField(max_length=200, blank=True, null=True) 
    institution_3 = models.CharField(max_length=200, blank=True, null=True) 
    institution_4 = models.CharField(max_length=200, blank=True, null=True) 
    employment_status = models.CharField(null=True, max_length=50, blank=True)
    present_position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    office_name = models.CharField(max_length=100, blank=True, null=True)
    office_address = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    office_country = models.CharField(max_length=100, blank=True, null=True)
    office_state =  models.CharField(max_length=100, blank=True, null=True)
    office_lga = models.CharField(max_length=100, blank=True, null=True)
    office_phone = models.CharField(max_length=100, blank=True, null=True)
    office_email = models.EmailField(blank=True, null=True)
    updated = models.BooleanField(default=False)
   
    state_of_origin =  models.CharField(max_length=100,  blank=True, null=True)
    lga_of_origin = models.CharField(max_length=100,  blank=True, null=True)
    
    gender = models.CharField(max_length=10, blank=True, null=True)

