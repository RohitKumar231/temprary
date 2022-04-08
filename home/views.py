from django.shortcuts import render
from django.db import connection


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def update_cancle(request):
    appointment_id = request.GET['appointment_id']
    name = request.GET['name']
    cursor = connection.cursor()
    query2 = "select * from sign_appointment where id='" + appointment_id + "'"
    cursor.execute(query2)
    data = cursor.fetchone()
    data = {'appointment_id':data[0], 'timedate': data[1], 'worker_id': data[4]}
    return render(request, 'Update_cancle.html',data)
def update(request):
    appointment_id = request.GET['appointment_id']
    time = request.GET['timedate']
    cursor = connection.cursor()
    query = "update sign_appointment set Appointment_date=%s where id='" + appointment_id + "'"
    value = (str(time))
    cursor.execute(query, value)
    return render(request,"end_page.html",{'message':"Your appointment has been updated"})
def cancle(request):
    appointment_id= request.GET['appointment_id']
    cursor = connection.cursor()
    query = "delete from sign_appointment where id='" + appointment_id + "'"
    cursor.execute(query)
    return render(request, "end_page.html",{'message':"Your appointment has been Canceled"})

def new_appointment(request):
    return render(request, "index.html")