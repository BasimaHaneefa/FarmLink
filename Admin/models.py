from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)


#category
class tbl_Product_Category(models.Model):
    Product_Category=models.CharField(max_length=20)




#Admin Registration
class tbl_Admin_Registration(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_contact=models.CharField(max_length=10)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=20)

#Place
class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)
    place_name=models.CharField(max_length=20)


class tbl_marketupdate(models.Model):
    product_name=models.CharField(max_length=50)
    productcategory=models.ForeignKey(tbl_Product_Category,on_delete=models.CASCADE)
    market_rate=models.CharField(max_length=50)
    update_date=models.DateField(null=True)
    
class tbl_info(models.Model):
    info_details=models.CharField(max_length=100)
    info_date=models.DateTimeField()
    info_title=models.CharField(max_length=50)
    info_file=models.FileField(upload_to='InfoDocs/')