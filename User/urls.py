from django.urls import path,include
from User import views
app_name="webuser"
urlpatterns =[
    path('Home/',views.Home,name="Home"),

#####################################################

    path('myprofile/',views.Myprofile,name="Myprofile"),
    path('editprofile/',views.Editprofile,name="Editprofile"),
    path('Changepassword/',views.Changepassword,name="Changepassword"),
########################################################################

    path('SearchFarmer/',views.SearchFarmer,name="SearchFarmer"),
    path('AjaxFarmer/',views.AjaxFarmer,name="AjaxFarmer"),
    path('Product/<int:pid>',views.Product,name="Product"),
    path('AjaxProduct/',views.AjaxProduct,name="AjaxProduct"),
    path('Addcart/<int:pid>',views.Addcart,name="Addcart"),
    path('Mycart/',views.Mycart,name="mycart"),
    path('DelCart/<int:did>',views.DelCart,name="delcart"),
    path('CartQty/',views.CartQty,name="cartqty"),
    path('Pay/',views.Pay,name="Pay"),
#################################################################################
    
    path('ViewProductBooking/',views.ViewProductBooking,name="ViewProductBooking"),

#################################################################################
  
    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),

#################################################################################
    
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),
##################################################################################
    
    path("logout/",views. logout,name="logout"),


]