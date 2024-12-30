from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.conf import settings
import traceback

from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    form_contacto = FormularioContacto()

    if request.method == "POST":
        form_contacto = FormularioContacto(data= request.POST) 
        if form_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage("Mensaje desde App Django",
                                 "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n \n {}".format(nombre,email,contenido),
                                 "",[settings.EMAIL_HOST_USER],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print(traceback.format_exc()) 
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'form':form_contacto})
