var tabla = [
    {nombre: "Adrian", apellidos: "Alvarado Molina", cedula: 117040078},
    {nombre: "Reiner", apellidos: "Mejias Soto", cedula: 510239875},
    {nombre: "Bernardo", apellidos: "Kinderson Rojas", cedula: 257894358} 
]

window.onload = cargarEventos

function cargarEventos(){
    document.getElementById("mostrartabla").addEventListener("click", mostrarTabla, false)

}

function mostrarTabla(){
    var cuerpoTabla = document.getElementById('empleadostabla')

    cuerpoTabla.innerHTML = "<tr><td>Adrian</td><td>Alvarado Molina</td><td>117040078</td></tr>"
}