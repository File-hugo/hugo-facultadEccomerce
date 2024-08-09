from .Carro import Carro

# crea en context processor para que funcione en todas las urls
def carro(request):
    return {'carro': Carro(request)}