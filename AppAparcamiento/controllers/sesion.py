from database.migrations.conexionBDD import conectar
from flask import render_template, request, Flask

class sesion:
    def __init__(self):
        pass

    def home(self):
        return render_template('services/main.html')

    def posicionamiento(self):
        return render_template('services/posicionamiento.html')
        
    def horarios(self):
        return render_template('services/horarios.html')
    
    def personas(self):
        return render_template('services/personas.html')
    
    def camaras(self):
        return render_template('services/camaras.html')
    def cerrarSesion(self):
        pass