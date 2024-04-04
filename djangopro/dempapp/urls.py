from django.contrib import admin
from django.urls import path,include
from dempapp import views

urlpatterns = [
    path('',views.index,name='index'),
     path('index',views.index,name='index'),
     path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('logout',views.logout,name='logout'),
      path('destination_details/<str:city_name>',views.destination_details,name='destination_details'),
       path('search', views.search, name='search'),
        path('destination_details/pessanger_detail_def/',views.pessanger_detail_def,name='pessanger_detail'),
        path('destination_details/pessanger_detail_def/pessanger_detail_def',views.confirmation,name="confirmation"),
         path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'), 
]     