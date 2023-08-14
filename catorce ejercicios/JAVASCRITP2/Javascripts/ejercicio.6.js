/* Hacer un algoritmo para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe
que, si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas
entonces las horas extras se le pagarán a $25 por hora.    */


let horasT = prompt("Ingrese las horas trabajadas: ");

    let minimo = 20;
    let tarifaSuperior = 25;

    let paga;

    if (horasT < 41) {
      paga = horasT * minimo;
      alert("El total a pagar es de: " + paga + " dólares.");
    } else {
      paga = horasT * tarifaSuperior;
      alert("El total a pagar es de: " + paga + " dólares.");
    }