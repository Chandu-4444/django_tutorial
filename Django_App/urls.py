from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home,name='home'),
    path('contacts_page', views.contacts_page, name='contacts'),
    
    

]