from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm ,  AuthenticationForm
                                                         

# Create your views here.

class VRegistro(View):
    #El get es el que nos muestra el formulario
    def get(self,request):#Lo que renderiza el formulario
        
        form = UserCreationForm()
        context = {"form":form}
        return render(request,"registro/registro.html",context)
        
    #El post es el que gestiona el envio de informacion a traves del formulario
    def post(self,request): #envia los datos a la bd
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
                
            login(request, usuario)
        
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request,"registro/registro.html",{"form":form})

def close_session(request):
    logout(request)
    
    return redirect('Home')

def logear(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # Asignar los datos al formulario correctamente
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")    
    
    return render(request, "login/login.html", {"form": form})