from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Users
from django.contrib import messages


# Create your views here.
def signup_login(request):
    return render(request, 'login_signup.html')


def signup(request):
    name = request.POST.get("name")
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    mobile = request.POST.get("mob")
    address = request.POST.get("address")
    if Users.objects.filter(Email=email).exists():
        return render(request, 'login_signup.html')                  ####### Need to improve
    else:
        users = Users(name=name, mob=mobile, Address=address, Email=email, password=psw)
        users.save()
        Id = Users.objects.filter(Email=email)[0].id
        messages.success(request, 'Signup Success')         ############
        return render(request, 'index.html',{'user_id':Id})


def signin(request):
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    cursor = connection.cursor()
    query1 = "select * from sign_users where Email='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    query2 = "select * from sign_appointment where user_id='" + str(data[0]) + "'"
    cursor.execute(query2)
    data1 = cursor.fetchone()
    if data[5]==psw:
        data= {'user_id':data[0],'Name':data[1],'Contact_number':data[2],'Address':data[3],'Email':data[4],'Password':data[5],'appointment_id':data1[0],'timedate':data1[1],'worker_id':data[4]}
        return render(request,'profile.html',data)
    else:
        return redirect('signup_login')
