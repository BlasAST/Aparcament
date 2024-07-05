window.addEventListener('DOMContentLoaded',iniciar)

function iniciar(){
    cargarDatos();
}

function cargarDatos(){
    let formulario=document.querySelector('form');
    formulario.addEventListener('submit',enviarDatos)
}

function enviarDatos(evt){
    evt.preventDefault();
    let valores=evt.currentTarget.querySelectorAll('input');
    let nombre=valores[0].value.trim();
    let contrasenia=valores[1].value.trim();
    

    if (nombre && contrasenia){
        pedirDatosLogin(nombre,contrasenia);
    }else{
        mensaje('Debes de completar los campos','red');
    }

}

async function pedirDatosLogin(nombre,contrasenia){
    try {
        let resultado= await fetch('/login?nombre='+nombre+'&contrasenia='+contrasenia);
        if(!resultado) throw new Error('Ha ocurrido un error en el inicio de sesión')
            let datos= await resultado.json();
        creacionDeUsuario(datos);
            
    } catch (error) {
        console.log(error);
    }
}



function creacionDeUsuario(datos){
    if(datos.estado==true){
        mensaje('Sesion iniciada correctamente','green');
        setTimeout(()=>{window.location.href='/home'},2000)
        }else{
            mensaje('Usuario no encontrado','red');
        }
}




function mensaje(contenido,color){
    let mensaje=document.querySelector('.mensaje');
    mensaje.textContent=contenido;
    mensaje.style.backgroundColor=color;
    mensaje.classList.remove('d-none')
    setTimeout(()=>{mensaje.classList.add('d-none')},2500);

}