from django.contrib import admin
from django.urls import path
from Basics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Calculator/',views.calculation,name="calculation"),
    path('Largest_smallest/',views.largest_smallest,name="largest_smallest"),
    path('Ranklist/',views.mark,name="mark"),
    path('Salary/',views.Salary,name="Salary"),
]
