<!--Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
un médico determina si una persona tiene anemia o no, lo cual depende de su nivel
de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que
tiene una persona es menor que el rango que le corresponde, se determina su
resultado como positivo y en caso contrario como negativo. La tabla en la que el
médico se basa para obtener el resultado es la siguiente:
Edad: 0 - 1 mes 
Nivel:13 
Hemoglobina: 26 g%

Edad: >1 y <= 6 meses 
Nivel:10
Hemoglobina: 18 g%

Edad: 6 y <= 12 meses 
Nivel:11
Hemoglobina: 15 g%

Edad: 1 y < = 5 años 
Nivel:11.5
Hemoglobina: 15 g%

Edad: 5 y <= 10 años 
Nivel:12.6
Hemoglobina: 15.5 g%


Edad: 10 y <=  15 años 
Nivel:13
Hemoglobina: 15.5 g%

Edad: mujeres 
Nivel:12
Hemoglobina: 16 g%

Edad: hombres 
Nivel:14
Hemoglobina: 18 g%-->

<h1>Diagnóstico de Anemia</h1>
    <form method="post">
        <label for="edad">Edad:</label>
        <select name="edad">
            <option value="0-1">0 - 1 mes</option>
            <option value="1-6">>1 y <= 6 meses</option>
            <option value="6-12">6 y <= 12 meses</option>
            <option value="1-5">1 y <= 5 años</option>
            <option value="5-10">5 y <= 10 años</option>
            <option value="10-15">10 y <= 15 años</option>
            <option value="mujeres">Mujer</option>
            <option value="hombres">Hombre</option>
        </select><br><br>

        <label for="hemoglobina">Nivel de Hemoglobina (g%):</label>
        <input type="number" name="hemoglobina" step="0.01" required><br>
        
        <button type="submit" name="submit">Calcular</button>
    </form>

    <h2>Resultado del diagnóstico:</h2>
    <p>
    <?php
        if (isset($_POST['submit'])) {
            $edadSeleccionada = $_POST['edad'];
            $hemoglobina = floatval($_POST['hemoglobina']);
            $resultado = "";
            $errorMensaje = "";

            $rangos = array(
                "0-1" => array("min" => 13, "max" => 26),
                "1-6" => array("min" => 10, "max" => 18),
                "6-12" => array("min" => 11, "max" => 15),
                "1-5" => array("min" => 11.5, "max" => 15),
                "5-10" => array("min" => 12.6, "max" => 15.5),
                "10-15" => array("min" => 13, "max" => 15.5),
                "mujeres" => array("min" => 12, "max" => 16),
                "hombres" => array("min" => 14, "max" => 18)
            );

            if ($hemoglobina < 0) {
                $errorMensaje = "Error: dato no válido";
            } else if ($hemoglobina < $rangos[$edadSeleccionada]["min"]) {
                $resultado = "Positivo";
            } else if ($hemoglobina >= $rangos[$edadSeleccionada]["min"] && $hemoglobina <= $rangos[$edadSeleccionada]["max"]) {
                $resultado = "Negativo";
            } else {
                $resultado = "Persona Anormal";
            }

            if (!empty($errorMensaje)) {
                echo "<span style='color: red;'>$errorMensaje</span>";
            } else {
                echo "Resultado: $resultado";
            }
        }
    ?>
    </p>



