from flask import Flask, render_template,request,jsonify, session
from flask_session import Session
from controllers.index import index
from controllers.registro import registro
from controllers.sesion import sesion
from controllers.inicioSesion import inicioSesion

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.config['SECRET_KEY'] = 'supersecreto'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

index_controller = index()
registro_controller = registro()
sesion_controller = sesion()
inicioSesion_controller = inicioSesion()

def middelware():
    if not session.get('user'):
        return True
    
def middelwareExit():
    if session.get('user'):
        return True
    
# Rutas de Index
@app.route('/')
def index():
    if middelwareExit():
        session['user']=None
    return index_controller.index()

# Rutas de registro
@app.route('/registrarse')
def registrarse():
    if middelwareExit():
        session['user']=None
    return registro_controller.index()


@app.route('/newUser', methods=['GET'])
def newUser():
    nombre = request.args.get('nombre')
    contrasenia = request.args.get('contrasenia')
    resultado=registro_controller.comprobarExistencia(nombre, contrasenia)
    if resultado['estado'] == False:
        session['user']=nombre
    return jsonify(resultado)

# Rutas de inicioSesión
@app.route('/iniciarSesion')
def iniciar_sesion():
    if middelwareExit():
        session['user']=None
    return inicioSesion_controller.index()

@app.route('/login' , methods=['GET'])
def login():
    nombre= request.args.get('nombre')
    contrasenia= request.args.get('contrasenia')
    resultado=inicioSesion_controller.comprobarUser(nombre,contrasenia)
    if resultado:
        session['user']=nombre
    return jsonify(resultado)



# Rutas de sesión
@app.route('/home')
def home():
    if middelware():
        return render_template('index.html')
    return sesion_controller.home()
@app.route('/posicionamiento')
def posicionamiento():
    if middelware():
        return render_template('index.html')
    return sesion_controller.posicionamiento()

@app.route('/horarios')
def horarios():
    if middelware():
        return render_template('index.html')
    return sesion_controller.horarios()

@app.route('/personas')
def personas():
    if middelware():
        return render_template('index.html')
    return sesion_controller.personas()

@app.route('/camaras')
def camaras():
    if middelware():
        return render_template('index.html')
    return sesion_controller.camaras()

@app.route('/user')
def user():
    if middelware():
        return render_template('index.html')
    return jsonify(session.get('user'))


if __name__ == '__main__':
    app.run(debug=True)
