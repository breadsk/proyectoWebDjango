from django.shortcuts import render , redirect
from .forms import FormularioContacto
#from blog.models import Contacto

# Create your views here.
def contacto(request):
    
    formulario_contacto=FormularioContacto()
    
    if request.method == "POST":
        #Cargar en nuestro formulario la información la info 
        #que el usuario ha ido introduciendo
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            inf_form=miFormulario.cleaned_data
            
            send_mail(inf_form['asunto'], inf_form['mensaje'],
            inf_form.get('email','nicolas.programador@gmail.com'),
            ['nicolas.programador@gmail.com'])
            
            return redirect("/contacto/?valido")
    
    return render(request,"contacto/contacto.html",{
        "miFormulario":formulario_contacto
    })
