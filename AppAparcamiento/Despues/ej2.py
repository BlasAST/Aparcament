#
#
#
#
# 	#  Desarrollar una aplicación para facilitar el trabajo a un empleado
# 	#  aparca coches
# 	#  para que poniendo la matricula se almacene en una base de datos
# 	#  Se debe de guardar del coche la matricula, la marca, el color y el nombre del dueño
# 	#  del dueño se debe de guardar el nombre, apellidos, numero telefono, correo y dni.
# 	#  Tambien se debe de llevar la cuenta de cuanto tiempo ha estado el coche aparcado.
# 	#  el dia mes y año de entrada y salida.
#
#

# def main():
#     interfaz()
#     nombre_login=input("Ingresa tu nombre\n")
#     while True:
#         edad_login = input("Ingresa tu edad\n")
#         try:
#             edad_login= int(edad_login)
#             break
#         except ValueError:
#             print("Ingresa una numero valido porfavor")
#     my.execute('''
#     INSERT INTO SESIONES (nombre,edad) VALUES (%s,%s)
#     ''', (nombre_login, edad_login))
#     connection.commit()
#     print("Se ha guardado tu sesión ", nombre_login)
#
#
# if __name__ == '__main__':
#     main()
#
#     # app.run(debug=True)
#
# # @app.route('/registrarse', methods=['POST'])
# # def login():
# #     return redirect(url_for('login', filename='registrarse.html'))
#
