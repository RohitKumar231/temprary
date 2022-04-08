from ctypes import addressof
from sign.models import Workers
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def reg_page(request):
    return render(request,'registerpro.html')


def register(request):
    name = request.POST.get("workername")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    email = request.POST.get("email")
    psw = request.POST.get("pswname")
    gender = request.POST.get("gender")
    service = request.POST.get("service")
    if Workers.objects.filter(Email=email).exists():
        return render(request, 'registerpro.html')                    ####### Need to improve
    else:
        users = Workers(name=name, contact=contact, Address=address, Email=email, password=psw,service=service)
        users.save()
        messages.success(request, 'Signup Success')         ############
        return HttpResponse('Profile page')

