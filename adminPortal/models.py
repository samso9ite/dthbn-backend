from django.db import models
from authentication.models import User
from schPortal.models import *
from profPortal.models import Professional

# Create your models here.
class IndexLimit(models.Model):
    school = models.CharField(max_length=255)
    assigned_limit = models.CharField(max_length=255)
    year = models.CharField(max_length=50, blank=True, null=True) 
  
    def __str__(self):
        return self.assigned_limit

class examLimit(models.Model):
    school = models.CharField(max_length=10)
    assigned_limit = models.CharField(max_length=40)
    year = models.CharField(max_length=10, blank=True, null=True) 
  
    def __str__(self):
        return self.assigned_limit
    
class Restrictions(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    block = models.BooleanField(default=False)
    suspend = models.BooleanField(default=False)

class closeIndexing(models.Model):
    access = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

class closeExamRegistration(models.Model):
    access = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

class licenseModel(models.Model):
    prof = models.ForeignKey(User, on_delete=models.CASCADE, related_name='license', default="null")
    renewal_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=50)
    certificate = models.FileField(upload_to='images/license', null=True)

     