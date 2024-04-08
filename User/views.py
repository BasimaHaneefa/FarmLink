from django.shortcuts import redirect, render
from FarmerApp.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def Home(request):
    products=tbl_product.objects.all()
    farmers=tbl_farmer_registration.objects.filter(farmer_status=1)
    info=tbl_info.objects.all().order_by('-info_date')
    return render(request,"User/HomePage.html",{'data':products,'farmers':farmers,'info':info})
#############################################################

def Myprofile(request):
    pro=tbl_user_registration.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':pro})

def Editprofile(request):
    pro=tbl_user_registration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        pro.user_name=request.POST.get("uname")
        pro.user_email=request.POST.get("uemail")
        pro.user_contact=request.POST.get("ucontact")
        pro.user_address=request.POST.get("uaddress")
        pro.save()
        return  redirect("webuser:Myprofile")
    else:
        return render(request,"User/EditProfile.html",{'data':pro})

###############################################################################

def Changepassword(request):
    pro=tbl_user_registration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        Oldpass=pro.user_password
        current=request.POST.get("txtpass")
        new=request.POST.get("txtnew")
        confirm=request.POST.get("txtcon")
        if Oldpass == current:
            if new == confirm:
                pro.user_password=new
                pro.save()
                msg="Password Changed"
                return render(request,"User/ChangePassword.html",{'msg':msg})
            else:
                msg="Password Mismatch"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
            msg="Password Mismatch"
            return render(request,"User/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"User/ChangePassword.html")

########################################################################################
    
def SearchFarmer(request):
    district=tbl_district.objects.all()
    farmer=tbl_farmer_registration.objects.filter(farmer_status=1)
    return render(request,"User/SearchFarmer.html",{'dis':district,'farmers':farmer})

def AjaxFarmer(request):
    if request.GET.get("dis") != "" and request.GET.get("place") != "" :
        dis=tbl_district.objects.get(id=request.GET.get("dis"))
        place=tbl_place.objects.get(id=request.GET.get("place"))
        farmer=tbl_farmer_registration.objects.filter(farmer_status=1,farmer_place__district=dis,farmer_place=place)
        return render(request,"User/AjaxFarmer.html",{'farmers':farmer})
    elif request.GET.get("dis") != ""  :
        dis=tbl_district.objects.get(id=request.GET.get("dis"))
        farmer=tbl_farmer_registration.objects.filter(farmer_status=1,farmer_place__district=dis)
        return render(request,"User/AjaxFarmer.html",{'farmers':farmer})
    elif  request.GET.get("place") != "" :
        place=tbl_place.objects.get(id=request.GET.get("place"))
        farmer=tbl_farmer_registration.objects.filter(farmer_status=1,farmer_place=place)
        return render(request,"User/AjaxFarmer.html",{'farmers':farmer})
    else:
        farmer=tbl_farmer_registration.objects.filter(farmer_status=1)
        return render(request,"User/AjaxFarmer.html",{'farmers':farmer})
    
def Product(request,pid):
    farmer=tbl_farmer_registration.objects.get(id=pid)
    request.session["fid"]=farmer.id
    data=tbl_Product_Category.objects.all()
    pdata=tbl_product.objects.filter(farm=farmer)
    return render(request,"User/ViewProducts.html",{'data':data,'pdata':pdata})

def AjaxProduct(request):
    if request.GET.get("did") != "":
        farmer=tbl_farmer_registration.objects.get(id=request.session["fid"])
        ptype=tbl_Product_Category.objects.get(id=request.GET.get("did"))
        pdata=tbl_product.objects.filter(farm=farmer,productcategory=ptype)
        return render(request,"User/AjaxProduct.html",{'pdata':pdata})
    else:
        farmer=tbl_farmer_registration.objects.get(id=request.session["fid"])
        pdata=tbl_product.objects.filter(farm=farmer)
        return render(request,"User/AjaxProduct.html",{'pdata':pdata})

def Addcart(request,pid):
    if 'uid' in request.session:
        productdata=tbl_product.objects.get(id=pid)
        custdata=tbl_user_registration.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
         bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
         cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
         if cartcount>0:
          msg="Already added"
          return render(request,"User/SearchFarmer.html",{'msg':msg})
         else:
        
          tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
          msg="Already added"
          return render(request,"User/SearchFarmer.html",{'msg':msg})
        else:
           tbl_booking.objects.create(user=custdata)
           bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
           if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
             msg="Already added"
             return render(request,"User/SearchFarmer.html",{'msg':msg})
            else:
             tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
             msg="Already added"
             return render(request,"User/SearchFarmer.html",{'msg':msg})
    else:
          return redirect("Guest:Login")
    
def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     bookingdata.booking_totalamount=request.POST.get("carttotalamt")
     bookingdata.booking_status=1
     bookingdata.save()
     return redirect("webuser:Pay")
   else:
    customerdata=tbl_user_registration.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     return render(request,"User/MyCart.html",{'data':cartdata})
    else:
      return render(request,"User/MyCart.html")
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("webuser:mycart")
def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("webuser:mycart")

def Pay(request):
   bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
   amnt=bookingdata.booking_totalamount
   if request.method=="POST":
      bookingdata.booking_status=2
      bookingdata.save()
      return redirect("webuser:mycart")
   else:
        return render(request,"User/Payment.html",{'amnt':amnt})
   
###############################################################################
   
def ViewProductBooking(request):
   pro=tbl_user_registration.objects.get(id=request.session["uid"])
   data=tbl_cart.objects.filter(booking__user=pro,booking__booking_status__gte=2)
   return render(request,"User/viewProductBooking.html",{'data':data})

##################################################################################



def Complaint(request):
    customerdata=tbl_user_registration.objects.get(id=request.session["uid"])
    Complaint=tbl_complaint.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(user=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("webuser:Complaint")
    else:
        return render(request,"User/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("webuser:Complaint")

##########################################################################################

def Feedback(request):
    customerdata=tbl_user_registration.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("webuser:Feedback")
    else:
        return render(request,"User/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webuser:Feedback")   

#########################################################################################

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('Guest:Login')
    else:
        return redirect('Guest:Login')       

   

