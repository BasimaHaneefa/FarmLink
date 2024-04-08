from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from FarmerApp.models import *
# Create your views here.

def user_registration(request):
    user_data=tbl_user_registration.objects.all()
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user_registration.objects.create(user_name=request.POST.get("txtname"),
                                user_email=request.POST.get("txtemail"),
                                user_contact=request.POST.get("txtcontact"),
                                user_address=request.POST.get("txtaddress"),
                                user_photo=request.FILES.get("fileImage"),
                                user_proof=request.FILES.get("fileProof"),
                                user_password=request.POST.get("txtpwd"),
                                place=place)
        return render(request,"Guest/User_Registration.html",{"districtdata":district})
    else:
        return render(request,"Guest/User_Registration.html",{"districtdata":district})



def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})


####################################################################################################
def farmer_registration(request):
    farmer_data=tbl_farmer_registration.objects.all()
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_farmer_registration.objects.create(
            farmer_name=request.POST.get("txtname"),
            farmer_email=request.POST.get("txtemail"),
            farmer_contact=request.POST.get("txtcontact"),
            farmer_address=request.POST.get("txtaddress"),
            farmer_district=request.POST.get("sel_district"),
            farmer_place=request.POST.get("sel_place"),
            farmer_photo=request.FILES.get("txtfile"),
            farmer_proof=request.FILES.get("txtproof"),
            farmer_password=request.POST.get("txtpassword"))
        return render(request,"Guest/Farmer_Registration.html",{'data':farmer_data})
    else:
        return render(request,"Guest/Farmer_Registration.html",{'data':farmer_data,'district':district_data})

#####################################################################################################

def Login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        acount=tbl_Admin_Registration.objects.filter(admin_email=Email,admin_password=Password).count()
        fcount=tbl_farmer_registration.objects.filter(farmer_email=Email,farmer_password=Password,farmer_status=1).count()
        ucount=tbl_user_registration.objects.filter(user_email=Email,user_password=Password).count()
        if acount>0:
            admindata=tbl_Admin_Registration.objects.get(admin_email=Email,admin_password=Password)
            request.session["adminid"]=admindata.id
            return redirect("webadmin:Home")
        elif fcount>0:
            farmerdata=tbl_farmer_registration.objects.get(farmer_email=Email,farmer_password=Password,farmer_status=1)
            request.session["fid"]=farmerdata.id
            return redirect("webfarmer:Home")
        
        elif ucount>0:
            userdata=tbl_user_registration.objects.get(user_email=Email,user_password=Password)
            request.session["uid"]=userdata.id
            return redirect("webuser:Home")

        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")
    
########################################################################################################

def index(request):
    products=tbl_product.objects.all()
    farmers=tbl_farmer_registration.objects.filter(farmer_status=1)
    info=tbl_info.objects.all().order_by('-info_date')
    return render(request,"Guest/index.html",{'data':products,'farmers':farmers,'info':info})