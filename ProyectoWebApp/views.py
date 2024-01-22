from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):
    
    carro=Carro(request)
    
    return render(request,"ProyectoWebApp/home.html")


def tienda(request):
    
    return render(request,"ProyectoWebApp/tienda.html")

def contacto(request):
    
    return render(request,"ProyectoWebApp/contacto.html")
