from fileinput import close
from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def familia (request):
    return HttpResponse('Probando el familia')

def probandoTemplate(request):
    context = {
        'nombre':'Jesus',
        'apellido':'Perez'
    }
    return render(request, 'template1.html', context = context)
    # #miHtml = open("C:/Users/jperez/Documents/Django/proyectobase/templates/template1.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    # miContexto = Context()
    # # documento = plantilla.render(miContexto)
    # # return HttpResponse(documento)