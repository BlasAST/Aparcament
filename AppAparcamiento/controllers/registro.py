
from database.migrations.conexionBDD import conectar
from flask import render_template, request, jsonify

my, connection = conectar()


class registro():
    def __init__(self):
        pass

    def index(self):
        return render_template('registrarse.html')

    def comprobarExistencia(self,nombre,contrasenia):
        if nombre:
            my.execute('SELECT * FROM USERS WHERE NOMBRE = %s', (nombre,))
            user=my.fetchone()
            if user:
                return {'estado':True}
            else:
                my.execute('''
                    INSERT INTO USERS (nombre, contrasenia) VALUES (%s, %s);''', (nombre,contrasenia,))
                connection.commit()

                return {'estado':False}

