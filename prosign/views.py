from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from sign.models import Workers
from django.contrib import messages


# Create your views here.
def prosignup_login(request):
    return render(request, 'prologin_signup.html')

def prosignup(request):
    try:
        name = request.POST.get("workername")
        contact = request.POST.get("contact")
        address = request.POST.get("address")
        email = request.POST.get("email")
        psw = request.POST.get("pswname")
        gender = request.POST.get("gender")
        service = request.POST.get("service")
        if Workers.objects.filter(Email=email).exists():
            return render(request, 'prologin_signup.html')  ####### Need to improve
        else:
            workers = Workers(name=name, contact=contact, Address=address, Email=email, password=psw, service=service)
            workers.save()
            messages.success(request, 'Signup Success')  ############
            return HttpResponse('Profile page')

    except:
        return render(request, 'error.html')



def prosignin(request):
    try:
        psw = request.POST.get("psw")
        email = request.POST.get("email")
        cursor = connection.cursor()
        query1 = "select * from sign_workers where Email='" + email + "'"
        cursor.execute(query1)
        data = cursor.fetchone()
        query2 = "select * from sign_appointment where worker_id='" + str(data[0]) + "'"
        cursor.execute(query2)
        data1 = cursor.fetchone()
        if data[5] == psw:
            data = {'worker_id': data[0], 'Name': data[1], 'Contact_number': data[2], 'Address': data[3],
                    'Email': data[4], 'Password': data[5], 'appointment_id': data1[0], 'timedate': data1[1],
                    'user_id': data[4]}
            return render(request, 'proprofile.html', data)
        else:
            return redirect('signup_login')
    except:
        return render(request, 'error.html')


