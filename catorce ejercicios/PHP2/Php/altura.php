<form>
    <label for="iniciales">Iniciales:</label>
    <input type="text" id="iniciales" name="iniciales"><br><br>
    <label for="altura">Altura:</label>
    <input type="text" id="altura" name="altura"><br><br>
    <button type="button" onclick="calcularAltura()">Calcular</button>
  </form>
  <div id="resultado"></div>
  
<?php
function calcularAltura() {
  $altura = $_POST['altura'];
  $iniciales = $_POST['iniciales'];

  if (!is_numeric($iniciales) || strpos($altura, "-") !== false) {
    echo "Error, ingresa datos válidos";
    return;
  }

  if ($iniciales && $altura) {
    $porciones = explode(' ', $altura);

    if (is_numeric($altura)) {
      $alturaNumero = floatval($altura);
      $metros = floor($alturaNumero);
      $centimetros = round(($alturaNumero - $metros) * 100);
      $resultado = "Tus iniciales son: " . $iniciales . " y tu altura es de " . ($metros > 0 ? $metros . " centímetro" . ($metros !== 1 ? "s" : "") : "") . ($centimetros > 0 ? ($metros > 0 ? " con " : "") . $centimetros . " centímetro" . ($centimetros !== 1 ? "s" : "") : "");
      echo $resultado;
    } else if (count($porciones) === 2 && $porciones[1] === "cm" && is_numeric($porciones[0])) {
      $centimetros = intval($porciones[0]);
      $resultado = "Tus iniciales son: " . $iniciales . " y tu altura es de " . $centimetros . " cm";
      echo $resultado;
    } else if (count($porciones) === 2 && is_numeric($porciones[0]) && is_numeric($porciones[1])) {
      $metros = intval($porciones[0]);
      $centimetros = floatval($porciones[1]);
      $resultado = "Tus iniciales son: " . $iniciales . " y tu altura es de " . $metros . " metro" . ($metros !== 1 ? "s" : "") . ($centimetros > 0 ? " con " . $centimetros . " centímetro" . ($centimetros !== 1 ? "s" : "") : "");
      echo $resultado;
    } else {
      echo "Error, ingresa datos válidos";
    }
  } else {
    echo "Error, ingresa datos válidos";
  }
}
?>
