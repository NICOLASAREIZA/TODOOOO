/*  #Dadas las tres calificaciones de un estudiante en la materia de algoritmia, calcule:
#a. Determinar su promedio
#b. Indicar si el estudiante aprobó o no el curso.
#Un estudiante aprueba la materia si el promedio es mayor o igual a 70 puntos.
  */


function calcularPromedio() {
    let calificacion1 = parseFloat(document.getElementById("calificacion1").value);
    let calificacion2 = parseFloat(document.getElementById("calificacion2").value);
    let calificacion3 = parseFloat(document.getElementById("calificacion3").value);

    let resultado = document.getElementById("resultado");

    if (isNaN(calificacion1) || isNaN(calificacion2) || isNaN(calificacion3)) {
        resultado.innerHTML = "Error: Ingrese calificaciones válidas.";
    } else if (calificacion1 < 0 || calificacion1 > 100 || calificacion2 < 0 || calificacion2 > 100 || calificacion3 < 0 || calificacion3 > 100) {
        resultado.innerHTML = "Error: Las calificaciones deben estar entre 0 y 100.";
    } else {
        let promedio = (calificacion1 + calificacion2 + calificacion3) / 3;
        resultado.innerHTML = "Promedio: " + promedio.toFixed(2);

        if (promedio >= 70) {
            resultado.innerHTML += " - Aprobado";
        } else {
            resultado.innerHTML += " - Reprobado";
        }
    }
}


