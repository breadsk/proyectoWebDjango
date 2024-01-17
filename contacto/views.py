from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.conf import settings

from .forms import FormularioContacto

#from django.core.mail import send_mail
from django.core.mail import EmailMessage
#from blog.models import Contacto

# Create your views here.
def contacto(request):
    
    formulario_contacto=FormularioContacto()
    
    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["nicolas.programador@gmail.com"],reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?no-valido")
                                    
            #recipient_list = ['nicolas.programador@gmail.com', 'nicolas.programador@gmail.com']                        
            #send_mail(nombre,contenido,email,recipient_list)                        
            
    
    return render(request,"contacto/contacto.html",{
        "miFormulario":formulario_contacto,
    })
