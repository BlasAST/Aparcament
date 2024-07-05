numero=1
numero2=123
def leer():
    numeroNuevo=numero+numero2
    print(numeroNuevo)
leer()

class Coche():
    marca="BMW"
    def __init__(self,modelo,coche):
        self.modelo=modelo
        self.coche=coche
    def saludoCoche(self):
        print('Hola, soy el coche',self.coche)

pablo=Coche('Rempalago','Cochesini')
print(pablo.saludoCoche())
