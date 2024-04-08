from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=100)
    product_rate=models.CharField(max_length=50)
    product_image=models.FileField(upload_to='Productimage/')
    productcategory=models.ForeignKey(tbl_Product_Category,on_delete=models.CASCADE)
    farm=models.ForeignKey(tbl_farmer_registration,on_delete=models.CASCADE)
