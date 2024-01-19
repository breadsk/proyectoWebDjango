class Carro:        
    def __init__(self,request):
        #Almacenar la peticion actual para usarla mas adelante
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")#Construir carro de la compra para esta sesion
        #Carro va a ser un diccionario
        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro
            
    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen
            }
        else:
            #En el caso de que si este en el carro
            #Recorrer todas las claves valor que tenemos en el dict
            #comprobar sila clave corresponde a la del producto que estamos
            #Agregando y si asi es, la cantidad que definimos la
            #Incrementamos en 1
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]= value["cantidad"]+1
                    break#Ya no recorras mas
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar(self,producto):
        #primer ver si existe para poder eliminar
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
  
    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                   self.eliminar(producto) 
                break
        self.guardar_carro()
  
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        