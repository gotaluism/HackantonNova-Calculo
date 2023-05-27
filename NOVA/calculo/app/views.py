from django.shortcuts import render, redirect, get_object_or_404
#from .forms import SupletorioForm
from .models import *
from .forms import *
# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'formulario.html',{'form':SupletorioForm()})
    else:
        try:
            form = SupletorioForm(request.POST)
            form.save()
            return redirect('home') 
        except ValueError:
            return render(request,'formulario.html',{'form':SupletorioForm(),'error':'-'})   

def solicitud(request,):
    solicitudes = general.objects.all()
    return render(request,'solicitud.html',{'solicitudes':solicitudes})


def eliminarSolicitud(request,idEpik):
    solicitud = get_object_or_404(general, pk=idEpik)
    solicitud.delete()
    return redirect('/solicitud')

def aceptarSolicitud(request, idEpik):
    aceptar = get_object_or_404(general, pk=idEpik)
    aceptar.delete()
    return redirect('/solicitud')
    