from fileinput import close
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def familia (request):
    return HttpResponse('Probando el familia')

def probandoTemplate(self):
    miHtml = open("C:/Users/jperez/Documents/Django/proyectobase/templates/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)