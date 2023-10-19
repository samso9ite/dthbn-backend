from django.db import models
from authentication.models import User
from cities_light.models import Region
from cities_light.models import Country
from schPortal.models import LGA

# Create your models here.
class Professional(models.Model):
    profuser = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='profuser')
    profile_image = models.ImageField(upload_to='images/professional/prof_profile_img', null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    postal_address = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    residential_country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    residential_state = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_residential_state_new')
    residential_lga = models.ForeignKey(LGA, on_delete=models.SET_NULL,blank=True, null=True)
    residential_address = models.CharField(max_length=200, blank= True, null=True)
    marital_status = models.CharField(max_length=200, blank=True, null=True)
    maiden_name = models.CharField(max_length=200, blank=True, null=True)
    state_of_origin = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_state_of_origin_new')
    lga_state = models.ForeignKey(LGA,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_lga_state_new') 
    senatorial_district = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.CharField(max_length=30, blank=True, null=True)
    state_of_birth = models.ForeignKey(Region,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_state_of_birth_new')
    lga_of_birth = models.ForeignKey(LGA,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_lga_of_birth_new')
    qualification1 = models.CharField(max_length=200, blank=True, null=True)     
    qualification2 = models.CharField(max_length=200, blank=True, null=True)     
    qualification3 = models.CharField(max_length=200, blank=True, null=True) 
    qualification4 = models.CharField(max_length=200, blank=True, null=True) 
    prof_qualification1 = models.CharField(max_length=200, blank=True, null=True) 
    prof_qualification2 = models.CharField(max_length=200, blank=True, null=True) 
    prof_qualification3 = models.CharField(max_length=200, blank=True, null=True) 
    prof_qualification4 = models.CharField(max_length=200, blank=True, null=True) 
    employment_status = models.CharField(null=True, max_length=50, blank=True)
    present_position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    office_name = models.CharField(max_length=100, blank=True, null=True)
    office_address = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    office_country = models.ForeignKey(Country,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_officeCountry_new')
    office_state =  models.ForeignKey(Region,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_officeState_new')
    office_lga = models.ForeignKey(LGA,on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_officeLga_new')
    office_phone = models.CharField(max_length=100, blank=True, null=True)
    office_email = models.EmailField(blank=True, null=True)
    updated =models.BooleanField(default=False)
   
    state_of_origin =  models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_state_of_origin_new')
    lga_of_origin = models.ForeignKey(LGA, on_delete=models.SET_NULL, blank=True, null=True, related_name='prof_lgaOrigin_new')
    
    gender = models.CharField(max_length=10, blank=True, null=True)


