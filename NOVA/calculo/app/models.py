from django.db import models
from django.contrib.auth.models import User

class general(models.Model):
    idEpik = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    curso = models.CharField(max_length=4)
    #fechaMonitoria
    valMonitoria = models.BooleanField(default=False)
    valTaller = models.BooleanField(default=False)
    
    def __str__(self):
        return self.idEpik 

class taller(models.Model):
    idEpik = models.ForeignKey(general, on_delete=models.CASCADE)
    validado = models.BooleanField(default=False)

class monitoria(models.Model):
    idEpik = models.CharField(max_length=20, primary_key=True)
    fechaAsistencia = models.DateTimeField()