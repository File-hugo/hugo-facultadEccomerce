class Carro():
    def __init__(self, request):
        self.session = request.session

        # obtener la clave de sesión actual si existe
        carro = self.session.get('session_key')

        # si el usuario es nuevo o no tiene una clave de sesión, creamos la clave
        if 'session_key' not in request.session:
            carro = self.session['session_key'] = {}

        # el atributo carro de la clase Carro se asigna a la variable carro
        self.carro = carro

    def agregar(self, producto):
        # Aquí asumimos que producto tiene un atributo 'id'
        producto_id = str(producto.id)
        #print(carro._len__())
        if producto_id in self.carro:
            # si no hay nada en el carrro abajo el else lo agrega
            #pass
            self.carro[producto_id]['cantidad']+=1
        else:
            self.carro[producto_id] ={
            'precio': producto.precio,
            'titulo': producto.titulo,
            'cantidad':1,
            }
#precio es el atributo        
        self.session.modified = True
        
    # Imprime en consola mejor el carro y no <carrito.Carro.Carro object at...
    def limpiar(self):
        self.carro=self.session['session_key']={}
        #carro sera elemento de la sesion con la key igual a vacio
        self.session.modified=True#indica actualiza lo que pasa en la sesion
       
    def __str__(self):
        return f'El carro del usuario tiene {self.carro}'
    def __len__(self):
        cantidad=0
        for key, values in self.carro.items():
            cantidad+=values['cantidad']
        #return len(self.carro)
        return cantidad
    
    def borrar(self,producto):
        del self.carro[producto]
        self.session.modified=True
  