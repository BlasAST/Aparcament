window.addEventListener('DOMContentLoaded', () => {
    iniciar();

})

function iniciar() {
    creacionNuevoUser();

}

function creacionNuevoUser() {
    let formulario = document.querySelector('.newUser');
    formulario.addEventListener('submit', enviar);
    async function enviar(evt) {
        evt.preventDefault();
        let valores = evt.currentTarget.querySelectorAll('input');
        if (valores && valores[0].value && valores[1].value) {
            let nombre = valores[0].value.trim();
            let contrasenia = valores[1].value.trim();

            if (!nombre) {
                mensaje('Debes tener un nombre', 'red');
            } else {
                let datos = await acceso(nombre, contrasenia);
                formulario.reset();
            }
        } else mensaje('Completa la información', 'red');
    }
}


async function acceso(nombre, contrasenia) {
    try {
        let response = await fetch('/newUser?nombre=' + nombre + '&contrasenia=' + contrasenia);
        if (!response) throw new Error('Error en la creación de un nuevo usuario');
        mostrarCarga();
        await new Promise(res => setTimeout(res, 4000));
        let datos = await response.json();
        limpiar()
        creacionUsuario(datos);
    }
    catch (error) {
        console.log(error)
    }
}

function mostrarCarga() {

    let elemento = document.querySelector('.cargando')
    elemento.classList.remove('d-none');
}
function limpiar() {
    let elemento = document.querySelector('.cargando')
    elemento.classList.add('d-none');
}

function creacionUsuario(datos) {
    let estado = datos.estado;
    estado == false ? creadoUser() : mensaje('Selecciona otro nombre', 'red');
}

function creadoUser() {
    mensaje('Se ha creado correctamente', 'green')
    setTimeout(() => {
        window.location.href = '/home';
    }, 2000);
}

function mensaje(mensaje, color) {
    let elemento = document.querySelector('.notificacion');
    elemento.classList.remove('d-none');
    elemento.textContent = mensaje;
    elemento.style.backgroundColor = color;
    setTimeout(() => {
        elemento.classList.add('d-none');
    }, 2000)
}