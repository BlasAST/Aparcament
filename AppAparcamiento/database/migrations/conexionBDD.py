import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Aparcamiento',
            user='root',
            password='2410223'
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            my = connection.cursor()
            return my,connection
    except Error as e:
        print("Error al conectar a MySQL", e)
        return e
