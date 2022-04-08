from django.db import connection
from django.shortcuts import render

# Create your views here.
def appointment_page(request):
    user_id=request.POST.get('user_id')
    cursor = connection.cursor()
    query1 = "select * from sign_users where id='" + str(user_id) + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    query2 = "select * from sign_appointment where user_id='" + str(data[0]) + "'"
    cursor.execute(query2)
    data1 = cursor.fetchone()
    data= {'user_id':data[0],'Name':data[1],'Contact_number':data[2],'Address':data[3],'Email':data[4],'Password':data[5],'appointment_id':data1[0],'timedate':data1[1],'worker_id':data[4]}
    return render(request,'profile.html',data)

