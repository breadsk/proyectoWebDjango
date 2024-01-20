from django.shortcuts import render , redirect

from .carro import Carro
from tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    
    carro = Carro(request)
    
    #Con esto obtenemos ya el producto que queremos 
    #agregar al carro
    producto=Producto.objects.get(id=producto_id)
    imagen_url = producto.imagen.url
    
    print(carro)
            
    #Ahora hay que agregar este producto al carro
    carro.agregar(producto=producto)
    
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    
    #Creamos el carro
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    
    return redirect("Tienda")
    
def restar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto=producto)
    
    return redirect("Tienda")

def limpiar_carro():
    
    carro=Carro(request)
    carro.limpiar_carro()
    
    return redirect("Tienda")