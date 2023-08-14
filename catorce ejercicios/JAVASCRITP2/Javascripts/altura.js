function calcularAltura() {
  var altura = document.getElementById('altura').value;
  var iniciales = document.getElementById('iniciales').value;

  if (!isNaN(iniciales) || altura.includes("-")) {
    document.getElementById('resultado').innerHTML = "Error, ingresa datos válidos";
    return;
  }

  if (iniciales && altura) {
    var porciones = altura.split(' ');

    if (!isNaN(altura)) {
      var alturaNumero = parseFloat(altura);
      var metros = Math.floor(alturaNumero);
      var centimetros = Math.round((alturaNumero - metros) * 100);
      var resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + (metros > 0 ? metros + " centimetro" + (metros !== 1 ? "s" : "") : "") + (centimetros > 0 ? (metros > 0 ? " con " : "") + centimetros + " centímetro" + (centimetros !== 1 ? "s" : "") : "");
      document.getElementById('resultado').innerHTML = resultado;
    } else if (porciones.length === 2 && porciones[1] === "cm" && !isNaN(porciones[0])) {
      var centimetros = parseInt(porciones[0]);
      var resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + centimetros + " cm";
      document.getElementById('resultado').innerHTML = resultado;
    } else if (porciones.length === 2 && !isNaN(porciones[0]) && !isNaN(porciones[1])) {
      var metros = parseInt(porciones[0]);
      var centimetros = parseFloat(porciones[1]);
      var resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + metros + " metro" + (metros !== 1 ? "s" : "") + (centimetros > 0 ? " con " + centimetros + " centímetro" + (centimetros !== 1 ? "s" : "") : "");
      document.getElementById('resultado').innerHTML = resultado;
    } else {
      document.getElementById('resultado').innerHTML = "Error, ingresa datos válidos";
    }
  } else {
    document.getElementById('resultado').innerHTML = "Error, ingresa datos válidos";
  }
}
