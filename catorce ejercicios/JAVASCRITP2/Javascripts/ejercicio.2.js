/* Leer 3 número distintos y determinar cuál es el menor.     */


function calcular() {
    let numero1, numero2, numero3;

    numero1 = parseFloat(document.getElementById("numero1").value);
    numero2 = parseFloat(document.getElementById("numero2").value);
    numero3 = parseFloat(document.getElementById("numero3").value);

    let respuesta = document.getElementById("respuesta");

    if (isNaN(numero1) || isNaN(numero2) || isNaN(numero3)) {
        respuesta.innerHTML = "Por favor, ingrese números válidos en todos los campos.";
    } else if (numero1 === numero2 && numero1 === numero3) {
        if (numero1 > numero2 && numero1 > numero3) {
            respuesta.innerHTML = "Los tres números son iguales y el mayor es " + numero1 + ".";
        } else {
            respuesta.innerHTML = "Los tres números son iguales  ";
        }
    } else if (numero1 === numero2) {
        if (numero1 > numero3) {
            respuesta.innerHTML = "El primer y segundo número son iguales y mayores que " + numero3 + ".";
        } else {
            respuesta.innerHTML = "El primer y segundo número son iguales y menores que " + numero3 + ".";
        }
    } else if (numero1 === numero3) {
        if (numero1 > numero2) {
            respuesta.innerHTML = "El primer y tercer número son iguales y mayores que " + numero2 + ".";
        } else {
            respuesta.innerHTML = "El primer y tercer número son iguales y menores que " + numero2 + ".";
        }
    } else if (numero2 === numero3) {
        if (numero2 > numero1) {
            respuesta.innerHTML = "El segundo y tercer número son iguales y mayores que " + numero1 + ".";
        } else {
            respuesta.innerHTML = "El segundo y tercer número son iguales y menores que " + numero1 + ".";
        }
    } else if (numero1 < numero2 && numero1 < numero3) {
        respuesta.innerHTML = "El número " + numero1 + " es el menor de los tres.";
    } else if (numero2 < numero1 && numero2 < numero3) {
        respuesta.innerHTML = "El número " + numero2 + " es el menor de los tres.";
    } else {
        respuesta.innerHTML = "El número " + numero3 + " es el menor de los tres.";
    }
}