/* Leer dos números, determinar cuál es el mayor de los dos y mostrar ese número en pantalla con el mensaje “Es el número mayor”.    */


function Calcular() {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let print = document.getElementById("respuesta");

    if (isNaN(num1) || isNaN(num2)) {
      print.innerHTML = "Por favor, ingrese dos números válidos.";
    } else {
      if (num1 > num2) {
        print.innerHTML = "El primer número es mayor.";
      } else if (num2 > num1) {
        print.innerHTML = "El segundo número es mayor.";
      } else {
        print.innerHTML = "Los números son iguales.";
      }
    }
  }