from django.views.generic import TemplateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from doctor.models import Appointment
from doctor.forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def quick_appointmnet(request):
	group_name=Group.objects.all().filter(user = request.user)# se obtiene el grupo del usuario
	group_name=str(group_name[0]) # parseo string
	if "Patient" == group_name:
		user_name=request.user.get_username()
		appointment_list = Appointment.objects.all().order_by("-user")
		q=request.GET.get("q")#inico busqueda
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list# termina busqueda

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name
		}
		return render(request, 'patient_quick_appointmnet.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')


def patient(request):#codigo para mis citas
	group_name=Group.objects.all().filter(user = request.user)# se obtiene el usuario logueado
	group_name=str(group_name[0]) # parseo string
	if "Patient" == group_name:
		user_name=request.user.get_username()#se obtiene el nombre de usuario
		#se obtienen todos los appointment y se filtra por usuario
		appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with=user_name)
		q=request.GET.get("q")#inicio de busqueda
		if q:
			appointment_list=appointment_list.filter(user__first_name__icontains=q)
		else:
			appointment_list = appointment_list#termina busqueda

		appointments= {
		    "query": appointment_list,
		    "user_name":user_name,    
		}
		return render(request, 'patient.html', appointments )
	else:
		return redirect('http://127.0.0.1:8000/')

def appointment_book(request, id):#se lanza al pulsar boton agendar
	group_name=Group.objects.all().filter(user = request.user)# se obtiene el grupo del usuario
	group_name=str(group_name[0]) # parseo string
	if "Patient" == group_name:
		user_name=request.user.get_username()
		single_appointment= Appointment.objects.get(id=id)
		form = single_appointment
		form.appointment_with=user_name
		form.save()
		return redirect('http://127.0.0.1:8000/patient/')
	else:
		return redirect('http://127.0.0.1:8000/')




