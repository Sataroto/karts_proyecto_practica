from django.shortcuts import render

from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    form_contacto = FormularioContacto()

    return render(request, "contacto/contacto.html", {'form':form_contacto})
