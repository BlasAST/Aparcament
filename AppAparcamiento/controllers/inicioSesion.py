from flask import Flask, jsonify,request,render_template
from database.migrations.conexionBDD import conectar

my,connection=conectar()

class inicioSesion():

    def __init__(self):
        pass

    def index(self):
        return render_template('iniciarSesion.html')
    
    def comprobarUser(self,nombre,contrasenia):
        if nombre and contrasenia:
            my.execute('''
                SELECT * FROM USERS WHERE nombre=%s and contrasenia=%s
            ''',(nombre,contrasenia))
            resultado=my.fetchone()
            if resultado:
                return {'estado':True}
            else:
                return {'estado':False}