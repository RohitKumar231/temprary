from django.db import connection
from django.shortcuts import render

# Create your views here.
def proappointment_page(request):
    try:
        worker_id = request.POST.get('worker_id')
        cursor = connection.cursor()
        query1 = "select * from sign_workers where id='" + str(worker_id) + "'"
        cursor.execute(query1)
        data = cursor.fetchone()
        query2 = "select * from sign_appointment where worker_id='" + str(data[0]) + "'"
        cursor.execute(query2)
        data1 = cursor.fetchone()
        data = {'worker_id': data[0], 'Name': data[1], 'Contact_number': data[2], 'Address': data[3], 'Email': data[4],
                'Password': data[5], 'appointment_id': data1[0], 'timedate': data1[1], 'user_id': data[4]}
        return render(request, 'proprofile.html', data)
    except:
        return render(request, 'error.html')




