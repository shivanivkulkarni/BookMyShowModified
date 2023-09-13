from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
import json
from django.http import JsonResponse
from authentication.models import *
from authentication.userBackend import *
from sellerApp.models import *
from adminApp.models import *

@csrf_exempt
def addSeller(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user_type = 'seller'    
        addSellerUser = CustomUser.objects.create_user(username = email, email = email,  password = password, user_type = user_type)
        user_id=addSellerUser.id
        addSeller = Seller(user_id = user_id, name = name)
        addSellerUser.save()
        addSeller.save()
        return JsonResponse({"msg":"Seller added successfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})
    
@csrf_exempt
def addAdmin(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user_type = 'admin'    
        addAdminUser = CustomUser.objects.create_user(username = email, email = email,  password = password, user_type = user_type)
        user_id=addAdminUser.id
        addAdmin = Admin(user_id = user_id, name = name)
        addAdminUser.save()
        addAdmin.save()
        return JsonResponse({"msg":"Admin added successfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})

@csrf_exempt
def sellerLogin(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        sellerLogin = CustomUser.objects.filter(username = email, user_type='seller')
        print(sellerLogin)
        if sellerLogin:
            seller = UserBackend().authenticate(request, username=email, password=password)
            print(seller)
            if seller is not None:
                seller.backend = 'django.contrib.auth.backends.ModelBackend'
                auth_login(request, seller)
                return JsonResponse({"msg": "Seller Login Successful"})
        else:
            return JsonResponse({"msg":"Please Enter Correct password or email"})

    except Exception as e:
        return JsonResponse({"msg":str(e)})

@csrf_exempt
def adminLogin(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        adminLogin = CustomUser.objects.filter(username = email, user_type='admin')
        print(adminLogin)
        if adminLogin:
            admin = UserBackend().authenticate(request, username=email, password=password)
            print(admin)
            if admin is not None:
                admin.backend = 'django.contrib.auth.backends.ModelBackend'
                auth_login(request, admin)
                return JsonResponse({"msg": "Admin Login Successful"})
        else:
            return JsonResponse({"msg":"Please Enter Correct password or email"})

    except Exception as e:
        return JsonResponse({"msg":str(e)})
