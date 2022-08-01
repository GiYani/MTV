
from django.http import HttpResponse
from MTVapp.models import Familia
from django.template import Template, Context

def familiar (request):
 family= Familia.objects.all()
 return HttpResponse (family[3].apellido)


def familiares (request):
    familiar={ 'nombre':['Gisele','Mauro','Gino'],'apellido':['Yani', 'manti', 'manti'], 'edad': [15,36,37]}

    archivo= open (r"C:\Users\PC\Desktop\PYTHON\DJANGO\mtv\proyecto_MTV\MTVapp\templates\familia.html","r")

    contenido= archivo.read()
    
    plantilla1=Template(contenido)
    
    context = Context(familiar)
    
    documento= plantilla1.render(context)
   
    return HttpResponse (documento)

