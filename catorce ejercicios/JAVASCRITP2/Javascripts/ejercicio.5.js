/* Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se desea calcular el
jornal diario de acuerdo con los siguientes puntos:
La tarifa de las horas diurnas es de 10 dólares.
La tarifa de las horas nocturnas es de 15 dólares.
Codifique un algoritmo que solicite el turno de trabajo y el número de horas trabajadas y
posteriormente calcule el valor a pagar.    */



    let turno = prompt("Ingrese el turno de trabajo (diurno/nocturno):");
    let horas = prompt("Ingrese el número de horas trabajadas:");

    let Diurna = 10;
    let Nocturna = 15;

    let valorAPagar;

    turno = turno.toLowerCase(); // Convertimos el valor ingresado a minúsculas

    if (turno === "diurno") {
        valorAPagar = horas * Diurna;
        alert("El total a pagar es de: " + valorAPagar + " dólares.");
    } else if (turno === "nocturno") {
        valorAPagar = horas * Nocturna;
        alert("El total a pagar es de: " + valorAPagar + " dólares.");
    } else {
        alert("El turno ingresado no es válido.");
    }
