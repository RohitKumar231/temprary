from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.prosignup_login, name= 'prosignup_login'),
    path('up/', views.prosignup, name= 'prosignup'),
    path('in/', views.prosignin, name= 'prosignin'),

]