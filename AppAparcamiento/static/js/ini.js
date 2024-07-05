window.addEventListener('DOMContentLoaded',()=>{
    iniciar();
})

function iniciar()
{
    eventosBotones();
}


function eventosBotones()
{
    let botonIniciarSesion=document.querySelector('#ini');
    let botonRegistrarse=document.querySelector('#reg');
    botonIniciarSesion.addEventListener('click',iniciarSesion);
    botonRegistrarse.addEventListener('click',registrarse);
}

function registrarse()
{

window.location.href='/registrarse';

}
function iniciarSesion(){
    console.log('Dentro2');
    window.location.href='/iniciarSesion';
}
