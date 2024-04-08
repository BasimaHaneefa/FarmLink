from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [
    path('district/',views.district,name="district"),
    path('deletedistrict/<int:Did>',views.Delete_District,name="Delete_District"),
    path('editdistrict/<int:eid>',views.Edit_District,name="Edit_District"),

################################################################################################

    path('product_category/',views.product_category,name="product_category"),
    path('deleteproduct_category/<int:pid>',views.Delete_product_category,name="Delete_product_category"),
    path('editproduct_category/<int:Pid>',views.edit_product_category,name="edit_product_category"),

################################################################################################

    path('registration/',views.admin_registration,name="admin_registration"),
    path('deleteregistration/<int:Rid>',views.Delete_Registration,name="Delete_Registration"),
    path('editregistration/<int:rid>',views.edit_registration,name="edit_registration"),

#################################################################################################

    path('place/',views.place,name="place"),
    path('delete_place/<int:pid>',views.delete_place,name="delete_place"),
    path('editplace/<int:eid>',views.edit_place,name="edit_place"),

####################################################################################################
   
     path('view_farmer_details/',views.View_farmer_Details,name="View_farmer_Details"),
     path('reject_farmer_registration/<int:rid>',views.reject_farmer_registration,name="reject_farmer_registration"),
     path('approve_farmer_registration/<int:eid>',views.approve_farmer_registration,name="approve_farmer_registration"),
     path('Accepted_farmer/',views.View_farmer_DetailsAccepted,name="View_farmer_DetailsAccepted"),
     path('Rejected_Farmer/',views.View_farmer_DetailsRejected,name="View_farmer_DetailsRejected"),

 ################################################################################################################################    
  
    # path('view_user_registration/',views.view_user_Registration,name="view_user_Registration"),
    # path('edit_user/',views.edit_user_registration,name="edit_user_registration"),
    # path('delet_user/',views.delete_user_registration,name="delete_user_registration"),
     
#########################################################################################################

    path('Home/',views.Home,name="Home"),

############################################################################################################
    
    path("ViewComplaint/",views. ViewComplaint,name="ViewComplaint"),
    path("Reply/<int:rid>",views. Reply,name="Reply"),

#############################################################################################################
    path("ViewFeedback/",views. ViewFeedback,name="ViewFeedback"),
#############################################################################################################
    path("logout/",views. logout,name="logout"),

#############################################################################################################
     
     path("Marketupdate/",views. Marketupdate,name="Marketupdate"),
     path("DeleteMarketupdate/<int:did>",views. DeleteMarketupdate,name="DeleteMarketupdate"),
     path("EditMarketupdate/<int:did>",views. EditMarketupdate,name="EditMarketupdate"),
     
#############################################################################################################
     path("Info/",views. Info,name="Info"),
     path("DeleteInfo/<int:did>",views. DeleteInfo,name="DeleteInfo"),
     ]