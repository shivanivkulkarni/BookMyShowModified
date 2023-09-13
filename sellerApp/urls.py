from django.contrib import admin
from django.urls import path,include
from sellerApp import views

urlpatterns = [
    path('api/addTheater',views.addTheater,name='addTheater')

]

