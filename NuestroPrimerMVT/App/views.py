from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from App.models import Familiar
from django.template import Template, context, loader

# Create your views here.

def familiar(request):

    familiar1 = Familiar(nombre="Martin Alejandro Gelaf", parentesco="Padre", dni="20430118", fechaDeNacimiento="1969-07-26")
    familiar1.save()

    familiar2 = Familiar(nombre="Maria Ines Echague", parentesco="Madre", dni="14386695", fechaDeNacimiento="1963-08-16")
    familiar2.save()

    familiar3 = Familiar(nombre="Florencia Cecilia Gelaf", parentesco="Hermana", dni="34997842", fechaDeNacimiento="1989-12-07")
    familiar3.save()

    plantilla = loader.get_template("template.html")

    familiares = [familiar1,familiar2,familiar3]

    a_mostrar = plantilla.render({"familiares":familiares})

    return HttpResponse(a_mostrar)
