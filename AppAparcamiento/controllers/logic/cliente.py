from logic.persona import Persona

class Cliente(Persona):

    def __init__(self, nombre, apellidos, dni,correo,numTelefono):
        super().__init__(nombre, apellidos, dni)
        correo=correo
        numTelefono=numTelefono
