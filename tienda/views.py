from django.shortcuts import render
from .models import Producto


# Create your views here.
def tienda(request):
    
    productos = Producto.objects.all()#Este es el select * from
    
    return render(request,"tienda/tienda.html",{
        "productos":productos
    })#Le envio el objeto