from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns =[

    path('NewUser/',views.user_registration,name="user_registration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

##################################################################

    path('add_farmer_registration/',views.farmer_registration,name="farmer_registration"),

##################################################################

    path('Login/',views.Login,name="Login"),

##################################################################

    path('',views.index,name="index"),
   
    
]
