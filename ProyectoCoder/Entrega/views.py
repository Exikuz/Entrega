from django.template import Template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from .models import familia
from datetime import datetime

def nuevo(self):
    nuevo1 = familia(Nombre="Juan", edad=18, nacimiento="2005-06-02")
    nuevo2 = familia(Nombre="Pedro", edad=34, nacimiento="1990-12-23")
    nuevo3 = familia(Nombre="Diego", edad=57, nacimiento="1974-11-30")
    nuevo1.save()
    nuevo2.save()
    nuevo3.save()
    Valor = f"Familiares agregados:  integrante #1: {nuevo1.Nombre} edad:{nuevo1.edad}, Integrante #2:{nuevo2.Nombre} edad:{nuevo2.edad}, Integrante #3: :{nuevo3.Nombre} edad:{nuevo3.edad} "
    return HttpResponse(Valor)

def vista(href):
    url= open("C:/Users/worldalytics/Desktop/entrega #2/ProyectoCoder/ProyectoCoder/templates/vista1.html")
    plant = Template(url.read())
    url.close()
    micon = Context()
    doc=plant.render(micon)
    return HttpResponse(doc)
# Create your views here.
