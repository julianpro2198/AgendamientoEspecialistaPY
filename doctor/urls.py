from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import(
	doctor,
	doctor_appointment_list,
	appointment_delete,
	doctor_appointment_update,
	)





urlpatterns = [
    path('', views.doctor, name='doctor_home'),
    path('my_appointment/', views.doctor, name='doctor_appointment'),
    path('create_appointment/', views.doctor_appointment_list, name='doctor_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', doctor_appointment_update,name='doctor_appointment_update'),      
      
]

