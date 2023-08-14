/* Escribir un algoritmo que, ingresada una calificación del 1 al 10, muestre por pantalla el
siguiente mensaje. Cuando la calificación sea de 7 o superior mostrar “APROBADO” y si no
obtuvo esa calificación mostrar “REPROBADO”.    */

function validar() {
    let nota = document.getElementById("nota").value.trim();
    let respuesta = document.getElementById("respuesta");

    if (nota === "") {
        respuesta.innerHTML = "Por favor, ingresa un dato válido.";
    } else {
        nota = parseFloat(nota);
        if (isNaN(nota) || nota < 1 || nota > 10) {
            respuesta.innerHTML = "Error: La nota ingresada no es válida. Debe ser un número entre 1 y 10.";
        } else if (nota >= 7) {
            respuesta.innerHTML = "APROBADO";
        } else {
            respuesta.innerHTML = "REPROBADO";
        }
    }
}