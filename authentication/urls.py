from django.contrib import admin
from django.urls import path,include
from authentication import views

urlpatterns = [
    path('api/addSeller',views.addSeller,name='addSeller'),
    path('api/sellerLogin',views.sellerLogin,name='sellerLogin'),
    path('api/addAdmin',views.addAdmin,name='addAdmin'),
    path('api/adminLogin',views.adminLogin,name='adminLogin')
    # path('api/addBuyer',views.addBuyer,name='addBuyer'),
    
]

