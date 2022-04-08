from django.shortcuts import render
from sign.models import Workers, Appointment
# Create your views here.
def booking(request):
    workername = request.GET.get('name')
    service = request.GET.get('service')
    email = request.GET.get('email')
    userid = request.GET.get('userid')


    return render(request, 'booking_confirmation.html',{'workername':workername, 'service':service, 'email':email,'userid':userid})



def booking_done(request):
    workername = request.GET.get("WorkerName")
    service = request.GET.get("service")
    email = request.GET.get("email")
    userid = request.GET.get("userid")
    datetime = request.GET.get("datetime")
    Id = Workers.objects.filter(Email=email)[0].id
    appointment = Appointment(Appointment_date = datetime, completed = 0 ,worker_id= Id, user_id=userid)
    appointment.save()
    return render(request, 'booking_completed.html',{'workername':workername, 'service':service, 'datetime':datetime,'id':Id})