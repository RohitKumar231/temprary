from django.shortcuts import render

# Create your views here.
def appointment_page(request):
    return render(request,'profile.html')