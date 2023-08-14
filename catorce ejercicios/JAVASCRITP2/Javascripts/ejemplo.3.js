/* Diseñe un algoritmo que dado dos números A y B, determine si A es mayor, igual o menor a B. */

function compararNumeros() {
    let numeroA = parseFloat(document.getElementById("numeroA").value);
    let numeroB = parseFloat(document.getElementById("numeroB").value);

    let resultado = document.getElementById("resultado");

    if (isNaN(numeroA) || isNaN(numeroB)) {
        resultado.innerHTML = "Error: Ingrese números válidos en ambos campos.";
    } else {
        if (numeroA === numeroB) {
            resultado.innerHTML = " A es igual a  B.";
        } else if (numeroA < numeroB) {
            resultado.innerHTML = " A es menor que B.";
        } else {
            resultado.innerHTML = " A es mayor que B.";
        }
    }
}

