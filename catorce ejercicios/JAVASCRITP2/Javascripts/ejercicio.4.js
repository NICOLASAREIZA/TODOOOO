/* En un estacionamiento cobran $1.500 por hora. Diseñe un algoritmo que determine cuanto
debe pagar un cliente por el estacionamiento de su vehículo, conociendo el tiempo de
estacionamiento en horas.   */


let horas = prompt("Escribe la cantidad de horas:");
let total = horas * 1500;

if (horas === null) {
  // Si el usuario presiona "Cancelar" en el prompt
  alert("No ingresaste ningún valor.");
} else if (isNaN(horas)) {
  // Si el valor ingresado no es un número válido
  alert("Por favor, ingresa un valor válido.");
} else if (horas === "0") {
  // Si el valor ingresado es "0"
  alert("No tienes que pagar nada.");
} else if (horas > 0 && horas <= 1) {
  // Si el valor ingresado está entre 0 (exclusivo) y 1 (inclusive)
  alert("El total a pagar es de " + total + " por hora.");
} else {
  // Si el valor ingresado es mayor que 1
  total = horas * 1500; // Recalculamos el total por horas
  alert("El total a pagar es de " + total + " por " + horas + " horas.");
}

    