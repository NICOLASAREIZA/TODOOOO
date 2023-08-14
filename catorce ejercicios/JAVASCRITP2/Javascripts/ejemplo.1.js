/* Diseñar un algoritmo que dada la edad de una persona indique si es MAYOR o MENOR de edad. */



let edad = prompt("Ingrese su edad: ");

if (edad > 0 && edad <= 100) {
  if (edad >= 18) {
    alert("Usted tiene " + edad + " años, eres mayor de edad.");
  } else {
    alert("Usted tiene " + edad + " años, eres menor de edad.");
  }
} else {
  alert("ERROR: La edad debe ser un número mayor a 0 y menor o igual a 100.");
}
