from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *

class SupletorioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['idEpik'].widget.attrs.update({'class': 'form-control',})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control',})
        self.fields['mail'].widget.attrs.update({'class': 'form-control',})
        self.fields['curso'].widget.attrs.update({'class': 'form-control',})
        self.fields['valMonitoria'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['valTaller'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    class Meta:
        model = general
        fields = ['idEpik','nombre','mail','curso','valMonitoria','valTaller']
        labels = {
            'idEpik': 'ID EPIK',
            'nombre': 'Nombre',
            'mail':'Correo Institucional',
            'curso':'Curso de Cálculo',
            'valTaller': '¿Hiciste el taller?',
            'valMonitoria': '¿Fuiste a monitoría?',
            }   