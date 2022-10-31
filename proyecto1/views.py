from contextvars import Context
from datetime import datetime
from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido


def saludo(request):
    p1=Persona("Profesor Alex", "Muñoz")

    #nombre="Alexander"
    #apellido="Muñoz"cd 

    fecha_actual=datetime.datetime.now()

    doc_externo=open("proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo":fecha_actual})
    documento=plt.render(ctx)

    return HttpResponse(documento)



def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")

def dame_Fecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad,agno):

    #edadActual=38
    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)