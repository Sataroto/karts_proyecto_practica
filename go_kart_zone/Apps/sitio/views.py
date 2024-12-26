from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def inicio(request):
     
     return render(request, "sitio/inicio.html")

def tienda(request):
     
     return render(request, "sitio/tienda.html")