from django.contrib import admin
from django.urls import path,include
from adminApp import views

urlpatterns = [
    
    path('api/test',views.test,name='test')
    # path('api/addAdmin',views.addAdmin,name='addAdmin')   
]

