from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user_registration(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_password=models.CharField(max_length=50)
    user_status = models.IntegerField(default="0")
    
####################################################################
class tbl_farmer_registration(models.Model):
    farmer_name=models.CharField(max_length=20)
    farmer_email=models.CharField(max_length=20)   
    farmer_contact=models.CharField(max_length=20)
    farmer_address=models.CharField(max_length=20)
    farmer_place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    farmer_photo=models.FileField(upload_to='farmers/photo/')
    farmer_proof=models.FileField(upload_to='farmers/proof/')
    farmer_password=models.CharField(max_length=20)
    farmer_status = models.IntegerField(default="0")