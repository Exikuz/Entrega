
from django.template import Template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from Entrega.models import familia2

def nuevo(self):
    nuevo = familia2(Nombre="alex",Edad =45, cumple= 0)
    nuevo.save()
    Valor = f"nuevo valor agregado {familia2.Nombre}"
    return HttpResponse(Valor)

