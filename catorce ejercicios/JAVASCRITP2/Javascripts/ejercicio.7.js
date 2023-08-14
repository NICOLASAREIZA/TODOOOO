/* A un trabajador le descuentan de su sueldo el 12% si su sueldo es menor o igual a 500000, por
encima de 500000 y hasta 1000000 el 15%, y por encima de 1000000 el 18%. Realice un
algoritmo que calcule el descuento y sueldo total que recibe el trabajador dado su sueldo
inicial.    */


let sueldo = prompt("Ingrese su sueldo");

if (sueldo === "-1") {
    alert("El sueldo ingresado es -1. El programa ha finalizado.");
} else {
    sueldo = parseInt(sueldo); // Convertir la entrada a número entero

    if (sueldo < -1) {
        alert("Error, dato no válido");
    } else if (sueldo <= 500000 && sueldo > 0) {
        totalmenos = sueldo - (sueldo * 0.12);
        alert("Su sueldo con el descuento es de " + totalmenos);
    } else if (sueldo <= 1000001) {
        totalmedio = sueldo - (sueldo * 0.15);
        alert("El sueldo con el descuento es igual a " + totalmedio);
    } else {
        totalmayor = sueldo - (sueldo * 0.18);
        alert("El sueldo con el descuento es igual a " + totalmayor);
    }
}
