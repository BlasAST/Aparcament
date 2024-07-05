from conexionBDD import conectar

my,connection = conectar()


class Empleado:
    def __init__(self, nombre, apellidos, numeroTelefono, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numeroTelefono = numeroTelefono
        self.correo = correo


class Cliente:
    def __init__(self, nombre, apellidos, numeroTelefono, correo, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numeroTelefono = numeroTelefono
        self.correo = correo
        self.dni = dni


class Coche:
    def __init__(self, matricula, marca, color, nombreDuenio):
        self.matricula = matricula
        self.marca = marca
        self.color = color
        self.nombreDuenio = nombreDuenio


def interfaz():
    print("Hola buenas tardes")
    my.execute("SHOW TABLES LIKE 'EMPLEADOS'")
    if not my.fetchone():
        my.execute('''
        CREATE TABLE EMPLEADOS(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            apellidos VARCHAR(255) NOT NULL,
            numeroTelefono VARCHAR(255) NOT NULL,
            correo VARCHAR(255) NOT NULL

        )''')
        print("Se ha creado la tabla de empleados")
    else:
        print("Ya existe la tabla empleados")
    my.execute("SHOW TABLES LIKE 'CLIENTES'")
    if not my.fetchone():
        my.execute('''
               CREATE TABLE CLIENTES(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(255) NOT NULL,
                   apellidos VARCHAR(255) NOT NULL,
                   numeroTelefono VARCHAR(255) NOT NULL,
                   correo VARCHAR(255) NOT NULL,
                   dni VARCHAR(255) NOT NULL
               )
               ''')
        print("Se ha creado la tabla clientes")
    else:
        print("Ya existe la tabla clientes")
    my.execute("SHOW TABLES LIKE 'COCHES'")
    if not my.fetchone():
        my.execute('''
        CREATE TABLE COCHES(
        id INT AUTO_INCREMENT PRIMARY KEY,
        matricula VARCHAR(255) NOT NULL,
        marca  VARCHAR(255) NOT NULL,
        color VARCHAR(255) NOT NULL,
        modelo VARCHAR(255) NOT NULL,
        id_cliente INT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id)
        )
        ''')
        print("Se ha creado la tabla de coches")
    else:
        print("Ya existe la tabla de coches")

    my.execute("SHOW TABLES LIKE 'USERS'")
    if not my.fetchone():
        my.execute('''
        CREATE TABLE USERS(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        contrasenia VARCHAR(255) NOT NULL
        )
        ''')
        print("Se ha creado la tabla de sesiones")
    else:
        print("Ya existe la tabla de sesiones")


def main():
    interfaz()


main()
