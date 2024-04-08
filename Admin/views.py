from datetime import datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from User.models import tbl_complaint, tbl_feedback

# Create your views here.
def district(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("district"))
        return render(request,"Admin/District.html",{'data':districtdata})
    else:
        return render(request,"Admin/District.html",{'data':districtdata})   

def Delete_District(request,Did):
    tbl_district.objects.get(id=Did).delete()
    return redirect("webadmin:district")

def Edit_District(request,eid):
    edit_data=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        edit_data.district_name=request.POST.get("district")
        edit_data.save()
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{'Data':edit_data})

######################################################################################################

#category
def product_category(request):
    productcategory_data=tbl_Product_Category.objects.all()
    if request.method=="POST":
        tbl_Product_Category.objects.create(Product_Category=request.POST.get("txtproductcategory"))
        return render(request,"Admin/Product_Category.html",{'Saved':productcategory_data})
    else:
        return render(request,"Admin/Product_Category.html",{'Saved':productcategory_data})

def Delete_product_category(request,pid):
    tbl_Product_Category.objects.get(id=pid).delete()
    return redirect("webadmin:product_category")


def edit_product_category(request,Pid):
    productcategory_data= tbl_Product_Category.objects.get(id=Pid)
    if request.method=="POST":
        productcategory_data.Product_Category=request.POST.get("txtproductcategory")
        productcategory_data.save()
        return redirect("webadmin:product_category")
    else:
        return render(request,"Admin/Product_Category.html",{'saved':productcategory_data})
    
##########################################################################################################

#Admin Registration
def admin_registration(request):
    registrationdata=tbl_Admin_Registration.objects.all()
    if request.method=="POST":
        tbl_Admin_Registration.objects.create(Name=request.POST.get("txtname"),Contact=request.POST.get("txtcontact"),Email=request.POST.get("txtemail"),Password=request.POST.get("txtpassword"))
        return render(request,"Admin/Admin_Registration.html",{'data':registrationdata})
    else:
        return render(request,"Admin/Admin_Registration.html",{'data':registrationdata})

def Delete_Registration(request,Rid):
    tbl_Admin_Registration.objects.get(id=Rid).delete()
    return redirect("webadmin:admin_registration")

def edit_registration(request,rid):
    registration_data=tbl_Admin_Registration.objects.get(id=rid)
    if request.method=="POST":
        registration_data.Name=request.POST.get("txtname")
        registration_data.Contact=request.POST.get("txtcontact")
        registration_data.Email=request.POST.get("txtemail")
        registration_data.Password=request.POST.get("txtpassword")
        registration_data.save()
        return redirect("webadmin:admin_registration")
    else:
        return render(request,"Admin/Admin_Registration.html",{'datas':registration_data})

##################################################################################################################

#place
def place(request):
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.all()
    if request.method=="POST":
        data=tbl_district.objects.get(id=request.POST.get('district'))
        tbl_place.objects.create(district=data,place_name=request.POST.get("txtplace"))
        return render(request,"Admin/Place.html",{'data':place_data,'dis':district_data})
    else:
        return render(request,"Admin/Place.html",{'data':place_data,'dis':district_data})

def delete_place(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("webadmin:place")

def edit_place(request,eid):
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        data=tbl_district.objects.get(id=request.POST.get('district'))
        place_data.district=data
        place_data.place_name=request.POST.get("txtplace")
        place_data.save()
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{'bata':place_data,'dis':district_data})

##################################################################################################

def View_farmer_Details(request):
    farmer_data=tbl_farmer_registration.objects.filter(farmer_status=0)
    return render(request,"Admin/Farmer_Verification.html",{'data':farmer_data})

def reject_farmer_registration(request,rid):
    farm=tbl_farmer_registration.objects.get(id=rid)
    farm.farmer_status=2
    farm.save()
    return redirect("webadmin:View_farmer_Details")

def approve_farmer_registration(request,eid):
    farmer_data=tbl_farmer_registration.objects.get(id=eid)
    farmer_data.farmer_status=1
    farmer_data.save()
    return redirect("webadmin:View_farmer_Details")

def View_farmer_DetailsAccepted(request):
    farmer_data=tbl_farmer_registration.objects.filter(farmer_status=1)
    return render(request,"Admin/Accepted_farmer.html",{'data':farmer_data})


def View_farmer_DetailsRejected(request):
    farmer_data=tbl_farmer_registration.objects.filter(farmer_status=2)
    return render(request,"Admin/Rejected_Farmer.html",{'data':farmer_data})
###########################################################################################

# def view_user_Registration(request):
#     view_user_data=tbl_user_registration.objects.all()
#     district = tbl_district.objects.all()
#     if request.method=="POST":
#         return render(request,"Admin/View_user_registration.html",{"districtdata":district})
#     else:
#         return render(request,"Admin/View_user_registration.html",{"districtdata":district})

# def delete_user_registration(request,did):
#     tbl_user_registration.objects.get(id=did).delete()
#     return redirect("Guest:view_user_Registration")
    
# def edit_user_registration(request,eid):
#     edit_user_data= tbl_user_registration.objects.get(id=eid)
#     if request.method=="POST":
#         edit_user_data.user_name=request.POST.get("txtname")
#         edit_user_data.user_email=request.POST.get("txtemail")
#         edit_user_data.user_contact=request.POST.get("txtcontact")
#         edit_user_data.user_address=request.POST.get("txtaddress")
#         edit_user_data.user_place=request.POST.get("sel_place")
#         edit_user_data.user_photo=request.POST.get("fileImage")
#         edit_user_data.user_proof=request.POST.get("fileproof")
#         edit_user_data.user_password=request.POST.get("txtpwd")
#         edit_user_data.save()
#         return redirect("Guest:view_user_Registration")
#     else:
#         return render(request,"Guest/User_Registration.html")
        
##########################################################################################

def accept_farmer(request):
    accepted_farmer_data=tbl_farmer_registration.objects.all()
    if request.method=="POST":
        return render(request,"Admin/Accepted_farmer.html",{'data':accepted_farmer_data})
    else:
        return render(request,"Admin/Accepted_farmer.html",{'data':accepted_farmer_data})

##########################################################################################

def Home(request):
    return render(request,"Admin/HomePage.html")

###########################################################################################

def ViewComplaint(request):
    newcom=tbl_complaint.objects.filter(complaint_status=0)
    recom=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{'new':newcom,'repl':recom})  
def Reply(request,rid):
    com=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtpro")
        com.complaint_status=1
        com.save()
        return redirect("webadmin:ViewComplaint")
    else:
        return render(request,"Admin/Reply.html")
    
#######################################################################################################
    
def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'data':data})     

#####################################################################################################

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        return redirect('Guest:Login')
    else:
        return redirect('Guest:Login')    

###################################################################################################

def Marketupdate(request):
    data=tbl_Product_Category.objects.all()
    product=tbl_marketupdate.objects.all()
    if request.method=="POST":
        seldata=tbl_Product_Category.objects.get(id=request.POST.get("selcat"))
        tbl_marketupdate.objects.create(product_name=request.POST.get("txtproduct"),
                                        productcategory=seldata,
                                        market_rate=request.POST.get("rate"),
                                        update_date=timezone.now().date() )
        return redirect("webadmin:Marketupdate")
    else:
        return render(request,"Admin/MarketProductUpdate.html",{'ProductType':data,'product':product})       

def DeleteMarketupdate(request,did):
        tbl_marketupdate.objects.get(id=did).delete()
        return redirect("webadmin:Marketupdate")

def EditMarketupdate(request,did):
    pdata=tbl_Product_Category.objects.all()
    data=tbl_marketupdate.objects.get(id=did)
    if request.method=="POST":
        seldata=tbl_Product_Category.objects.get(id=request.POST.get("selcat"))
        data.product_name=request.POST.get("txtproduct")
        data.market_rate=request.POST.get("rate")
        data.productcategory=seldata
        data.update_date=timezone.now().date()
        data.save()
        return redirect("webadmin:Marketupdate")
    else:
        return render(request,"Admin/MarketProductUpdate.html",{'data':data,'ProductType':pdata})

#################################################################################################
    
def Info(request):
    data=tbl_info.objects.all().order_by('-info_date')
    if request.method=="POST":
        tbl_info.objects.create(info_title=request.POST.get("txttit"),
                                info_details=request.POST.get("txtdetails"),
                                info_file=request.FILES.get("file"),
                                info_date=datetime.now())
        return redirect("webadmin:Info")
    else:
        return render(request,"Admin/Info.html",{'data':data})
    
def DeleteInfo(request,did):
    tbl_info.objects.get(id=did).delete()
    return redirect("webadmin:Info")