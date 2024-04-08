from django.shortcuts import render,redirect
from FarmerApp.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def Home(request):
    pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
    products=tbl_product.objects.filter(farm=pro)
    
    return render(request,"FarmerApp/HomePage.html",{'data':products})
    
#######################################################################################

def Myprofile(request):
    pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
    return render(request,"FarmerApp/MyProfile.html",{'data':pro})

def  Editprofile(request):
    pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
    if request.method=="POST":
        pro.farmer_name=request.POST.get("fname")
        pro.farmer_email=request.POST.get("femail")
        pro.farmer_contact=request.POST.get("fcontact")
        pro.farmer_address=request.POST.get("address")
        pro.save()
        return  redirect("webfarmer:Myprofile")
    else:
        return render(request,"FarmerApp/EditProfile.html",{'data':pro})

def Changepassword(request):
    pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
    if request.method=="POST":
        Oldpass=pro.farmer_password
        current=request.POST.get("txtpass")
        new=request.POST.get("txtnew")
        confirm=request.POST.get("txtcon")
        if Oldpass == current:
            if new == confirm:
                pro.farmer_password=new
                pro.save()
                msg="Password Changed"
                return render(request,"FarmerApp/ChangePassword.html",{'msg':msg})
            else:
                msg="Password Mismatch"
                return render(request,"FarmerApp/ChangePassword.html",{'msg':msg})
        else:
            msg="Password Mismatch"
            return render(request,"FarmerApp/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"FarmerApp/ChangePassword.html")

############################################################################################
    
def Product(request):
    data=tbl_Product_Category.objects.all()
    pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
    pdata=tbl_product.objects.filter(farm=pro)
    if request.method=="POST":
        seldata=tbl_Product_Category.objects.get(id=request.POST.get("ProductType"))
        tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                   product_description=request.POST.get("txtdetails"),
                                   product_rate=request.POST.get("txtprice"),
                                   product_image=request.FILES.get("image"),
                                   farm=pro,productcategory=seldata)
        return redirect("webfarmer:Product")
    else:
        return render(request,"FarmerApp/Product.html",{'ProductType':data,'pdata':pdata})
    
def DeleteProduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect("webfarmer:Product")


#####################################################################################

def ViewProductBooking(request):
   pro=tbl_farmer_registration.objects.get(id=request.session["fid"])
   data=tbl_cart.objects.filter(product__farm=pro,booking__booking_status__gte=2)
   return render(request,"FarmerApp/viewProductBooking.html",{'data':data})

def UpdateBooking(request,bid):
    data=tbl_cart.objects.get(id=bid)
    if data.cart_status == '0':
        data.cart_status=1
        data.save()
        return redirect("webfarmer:ViewProductBooking")
    elif data.cart_status == '1':
        data.cart_status=2
        data.save()
        return redirect("webfarmer:ViewProductBooking")
    else:
        data.cart_status=3
        data.save()
        return redirect("webfarmer:ViewProductBooking")
    
#######################################################################################################

def logout(request):
    if 'fid' in request.session:
        del request.session['fid']
        return redirect('Guest:Login')
    else:
        return redirect('Guest:Login')     

########################################################################################################
    
def Infofeed(request):
    data=tbl_info.objects.all().order_by('-info_date')
    return render(request,"FarmerApp/Info.html",{'info_list':data})

#######################################################################################################

def MarketUpdate(request):
    data=tbl_marketupdate.objects.all()
    return render(request,"FarmerApp/MarketUpdate.html",{'marketupdates':data})