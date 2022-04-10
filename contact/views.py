from django.shortcuts import render
from .models import contactus


# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def contacts(request):
    try:
        firstname = request.GET.get("firstname")
        lastname = request.GET.get("lastname")
        subject = request.GET.get("subject")
        users = contactus(firstname=firstname, lastname=lastname, subject=subject)
        users.save()
        return render(request, 'contact.html')
    except:
        return render(request, 'error.html')

