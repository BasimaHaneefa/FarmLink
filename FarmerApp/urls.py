from django.urls import path,include
from FarmerApp import views
app_name="webfarmer"
urlpatterns =[
    path('Home/',views.Home,name="Home"),

##################################################

    path('myprofile/',views.Myprofile,name="Myprofile"),
    path('editprofile/',views.Editprofile,name="Editprofile"),
    path('Changepassword/',views.Changepassword,name="Changepassword"),
#############################################################################
    path('Product/',views.Product,name="Product"),
    path('DeleteProduct/<int:did>',views.DeleteProduct,name="DeleteProduct"),
   
#############################################################################
     
    path('ViewProductBooking/',views.ViewProductBooking,name="ViewProductBooking"),
    path('UpdateBooking/<int:bid>',views.UpdateBooking,name="UpdateBooking"),


#############################################################################################################
    path("logout/",views. logout,name="logout"),

############################################################################################################
    path("Infofeed/",views. Infofeed,name="Infofeed"),
###########################################################################################################
    path("MarketUpdate/",views. MarketUpdate,name="MarketUpdate"),

]
