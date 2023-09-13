from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def test(request):
    return JsonResponse({"msg":"test api"})
