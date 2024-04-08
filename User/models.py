from django.db import models
from Guest.models import *
from FarmerApp.models import *
# Create your models here.

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.CharField(default=0,max_length=10)
    user=models.ForeignKey(tbl_user_registration,on_delete=models.CASCADE)
    booking_totalamount=models.CharField(default=0,max_length=10)

class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_qty=models.CharField(max_length=50)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    cart_status=models.CharField(default=0,max_length=10)


class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_user_registration,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    user=models.ForeignKey(tbl_user_registration,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)

