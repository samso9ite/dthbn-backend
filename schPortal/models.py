from django.db import models
from authentication.models import User
from cities_light.models import Region
from cities_light.models import Country
from django.utils import timezone
import datetime
# Create your models here.

class LGA(models.Model):
    local_gov_area = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.local_gov_area

class School(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    sch_logo = models.FileField(upload_to='images/school/sch_logo', null=True)
    postal_number = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True,  null=True)
    region = models.CharField(max_length=200, blank=True)
    hod_name = models.CharField(max_length=200, blank=True)
    hod_phone = models.CharField(max_length=20, blank=True)
    hod_email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=True)
    exam_quota_count = models.IntegerField(null=True)
    index_quota_limit = models.IntegerField(null=True)
    exam_quota_limit = models.IntegerField(null=True)
    exam_quota_used = models.IntegerField(null=True)
    updated = models.BooleanField(default=False)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    close_exam_reg = models.BooleanField(default=False)
    closed_exam_date = models.DateTimeField(blank=True, null=True)
    close_index_reg = models.BooleanField(default=False)
    closed_index_date = models.DateTimeField(blank=True, null=True)


class Indexing(models.Model):
    profile_image = models.ImageField(upload_to='images/indexing/profile_img', null=True, blank=True)
    institution = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='institution')
    # school_add = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, related_name='index_school')
    cadre = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)    
    first_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    lga = models.CharField(max_length=200, blank=True, null=True)
    marital_status = models.CharField(max_length=200, blank=True, null=True)
    permanent_address= models.CharField(max_length=200, blank=True, null=True)
    place_of_work = models.CharField(max_length=200, blank=True, null=True)
    school_attended_1 = models.CharField(max_length=200, blank=True, null=True)     
    school_attended_2 = models.CharField(max_length=200, blank=True, null=True)     
    school_attended_3 = models.CharField(max_length=200, blank=True, null=True)     
    qualification_1 = models.CharField(max_length=200, blank=True, null=True)     
    qualification_2 = models.CharField(max_length=200, blank=True, null=True)     
    qualification_3 = models.CharField(max_length=200, blank=True, null=True) 
    admission_grad_year_1 = models.CharField(max_length=200, blank=True, null=True)
    admission_grad_year_2 = models.CharField(max_length=200, blank=True, null=True)
    admission_grad_year_3 = models.CharField(max_length=200, blank=True, null=True)  
    # graduation_year = models.CharField(max_length=200, blank=True, null=True) 
     
    contact_address = models.CharField(max_length=200, blank=True, null=True)       
    referee_name = models.CharField(max_length=200, blank=True, null=True) 
    referee_address = models.CharField(max_length=200, blank=True, null=True)  
    referee_number = models.CharField(max_length=200, blank=True, null=True)  
    referee_name_0 = models.CharField(max_length=200, blank=True, null=True) 
    referee_address_2 = models.CharField(max_length=200, blank=True, null=True)  
    referee_number_1 = models.CharField(max_length=200, blank=True, null=True)  
    marriage_cert = models.ImageField(upload_to='images/indexing/marriage_cert', null=True, blank=True)
    o_level_cert = models.ImageField(upload_to='images/OlevelResult',  null=True, blank=True)
    o_level_cert_0 = models.ImageField(upload_to='images/OlevelResult',  null=True, blank=True)
    exam_number = models.CharField(max_length=100, null=True, blank=True)
    exam_year = models.CharField(max_length=20, null=True, blank=True)
    exam_type = models.CharField(max_length=20, null=True, blank=True)
    exam_number_0 = models.CharField(max_length=100, null=True, blank=True)
    exam_year_0 = models.CharField(max_length=20, null=True, blank=True)
    exam_type_0 = models.CharField(max_length=20, null=True, blank=True)
    sub_1 = models.CharField(max_length=20, null=True, blank=True)
    grade_1 = models.CharField(max_length=20, null=True, blank=True)
    sub_2 = models.CharField(max_length=20, null=True, blank=True)
    grade_2 = models.CharField(max_length=20, null=True, blank=True)
    sub_3 = models.CharField(max_length=20, null=True, blank=True)
    grade_3 = models.CharField(max_length=20, null=True, blank=True)
    sub_4 = models.CharField(max_length=20, null=True, blank=True)
    grade_4 = models.CharField(max_length=20, null=True, blank=True)
    sub_5 = models.CharField(max_length=20, null=True, blank=True)
    grade_5 = models.CharField(max_length=20, null=True, blank=True)
    sub_6 = models.CharField(max_length=20, null=True, blank=True)
    grade_6 = models.CharField(max_length=20, null=True, blank=True)
    sub_7 = models.CharField(max_length=20, null=True, blank=True)
    grade_7 = models.CharField(max_length=20, null=True, blank=True)
    sub_1_0 = models.CharField(max_length=20, null=True, blank=True)
    grade_1_0 = models.CharField(max_length=20, null=True, blank=True)
    grade_2_1 = models.CharField(max_length=20, null=True, blank=True)
    sub_2_1 = models.CharField(max_length=20, null=True, blank=True)
    sub_3_2 = models.CharField(max_length=20, null=True, blank=True)
    grade_3_2 = models.CharField(max_length=20, null=True, blank=True)
    sub_4_3 = models.CharField(max_length=20, null=True, blank=True)
    grade_4_3 = models.CharField(max_length=20, null=True, blank=True)
    sub_5_4 = models.CharField(max_length=20, null=True, blank=True)
    grade_5_4 = models.CharField(max_length=20, null=True, blank=True)
    sub_6_5 = models.CharField(max_length=20, null=True, blank=True)
    grade_6_5 = models.CharField(max_length=20, null=True, blank=True)
    grade_7_6 = models.CharField(max_length=20, null=True, blank=True)
    sub_7_2 = models.CharField(max_length=20, null=True, blank=True)
    submitted = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    unapproved = models.BooleanField(default=False)
    comment = models.CharField(max_length=500, blank=True, null=True)
    exam_sitting = models.CharField(max_length=5, null=False, blank=True)
    verified = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)   
    grade3_2 = models.CharField(max_length=20, null=True, blank=True)
   
    def __str__(self):
        return self.first_name

class ExamRegistration(models.Model):
    profile_image = models.ImageField(upload_to='images/exam/exam_profile_img', null=True, blank=True)
    institute = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='school')
    verified = models.BooleanField(default=False)
    title = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    # state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    postal_address = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    residential_country = models.CharField(max_length=100, blank=True, null=True)
    residential_state = models.CharField(max_length=100, blank=True, null=True)
    residential_lga = models.CharField(max_length=100, blank=True, null=True)
    residential_address = models.CharField(max_length=200, blank= True, null=True)
    marital_status = models.CharField(max_length=200, blank=True, null=True)
    maiden_name = models.CharField(max_length=200, blank=True, null=True)
    state_of_origin = models.CharField(max_length=200, blank=True, null=True) 
    lga_state = models.CharField(max_length=200, blank=True, null=True) 
    senatorial_district = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    state_of_birth = models.CharField(max_length=200, blank=True, null=True)
    lga_of_birth = models.CharField(max_length=200, blank=True, null=True)
    qualifications = models.CharField(max_length=200, blank=True, null=True)     
    professional_qualifications = models.CharField(max_length=200, blank=True, null=True) 
    institutions_attended = models.CharField(max_length=200, blank=True, null=True) 
    hod_name = models.CharField(max_length=200, blank=True, null=True)
    hod_phone = models.CharField(max_length=20, blank=True, null=True)
    hod_email = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=100, blank=True, null=True)
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
    referees = models.CharField(max_length=200, blank=True, null=True) 
    year = models.CharField(max_length=10, null=True, blank=True)
    mode_of_payment = models.CharField(max_length=200, blank=True, null=True)
    cadre = models.CharField(max_length=200, blank=True, null=True)
    waec_result = models.ImageField(upload_to='images/exam_sector/waec_result', blank=True, null=True)
    dental_school_result = models.ImageField(upload_to='images/exam_sector/dental_result', blank=True, null=True)
    dental_school_testimonial = models.ImageField(upload_to='images/exam_sector/dental_testimonial', blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    submitted = models.BooleanField(default=False, blank=True)
    approved = models.BooleanField(default=False, blank=True)

    unapproved = models.BooleanField(default=False, blank=True)
    comment = models.CharField(max_length=500, blank=True, null=True)








