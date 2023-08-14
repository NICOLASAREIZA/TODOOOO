<!-- -->


<form method="post">
    <p>Seleccione su candidato:</p>
    <input type="radio" name="candidato" value="1">Sergio Mauricio Zúñiga<br>
    <input type="radio" name="candidato" value="2">Yider Luna Joven<br>
    <input type="radio" name="candidato" value="3">Franklin Alexander Vega<br>
    <input type="radio" name="candidato" value="4">Voto en blanco<br>
    <input type="submit" value="Votar">
</form>

<?php
// Comprobamos si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["candidato"])) {
        votar($_POST["candidato"]);
    } else {
        echo "Por favor, seleccione un candidato.";
    }
}

// Función para incrementar el voto del candidato seleccionado
function votar($candidato)
{
    if (!isset($_COOKIE['sergioVotes'])) {
        setcookie('sergioVotes', 0, time() + 3600);
    }
    if (!isset($_COOKIE['yiderVotes'])) {
        setcookie('yiderVotes', 0, time() + 3600);
    }
    if (!isset($_COOKIE['franklinVotes'])) {
        setcookie('franklinVotes', 0, time() + 3600);
    }
    if (!isset($_COOKIE['blankVotes'])) {
        setcookie('blankVotes', 0, time() + 3600);
    }

    switch ($candidato) {
        case 1:
            setcookie('sergioVotes', $_COOKIE['sergioVotes'] + 1, time() + 3600);
            break;
        case 2:
            setcookie('yiderVotes', $_COOKIE['yiderVotes'] + 1, time() + 3600);
            break;
        case 3:
            setcookie('franklinVotes', $_COOKIE['franklinVotes'] + 1, time() + 3600);
            break;
        case 4:
            setcookie('blankVotes', $_COOKIE['blankVotes'] + 1, time() + 3600);
            break;
        default:
            echo "Opción no válida";
            break;
    }

    // Redirigir después de votar para evitar problemas con el reenvío del formulario
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}

// Mostrar resultados solo después de votar
if (isset($_COOKIE['sergioVotes']) || isset($_COOKIE['yiderVotes']) || isset($_COOKIE['franklinVotes']) || isset($_COOKIE['blankVotes'])) {
    mostrarResultados();
} else {
    echo "Votos totales: 0<br>";
    echo "Ganador: No hay votos aún.";
}

// Función para mostrar el ganador y la cantidad de votos totales
function mostrarResultados()
{
    $sergioVotes = $_COOKIE['sergioVotes'] ?? 0;
    $yiderVotes = $_COOKIE['yiderVotes'] ?? 0;
    $franklinVotes = $_COOKIE['franklinVotes'] ?? 0;
    $blankVotes = $_COOKIE['blankVotes'] ?? 0;

    $votosTotales = $sergioVotes + $yiderVotes + $franklinVotes + $blankVotes;
    echo "Votos totales: $votosTotales<br>";

    $maxVotes = max([$sergioVotes, $yiderVotes, $franklinVotes]);
    $ganadores = [];

    if ($maxVotes === $sergioVotes) {
        $ganadores[] = "Sergio Mauricio Zúñiga";
    }
    if ($maxVotes === $yiderVotes) {
        $ganadores[] = "Yider Luna Joven";
    }
    if ($maxVotes === $franklinVotes) {
        $ganadores[] = "Franklin Alexander Vega";
    }

    if (count($ganadores) === 1) {
        echo "Ganador: " . $ganadores[0] . " con " . $maxVotes . " votos.";
    } else {
        echo "Empate: " . implode(', ', $ganadores) . " con " . $maxVotes . " votos cada uno.";
    }

    if ($blankVotes > 0) {
        echo "<br>Votos en blanco: " . $blankVotes;
    }
}
?>

<br>
<a href="?reset=true">Reiniciar Votos</a>

<?php
if (isset($_GET['reset']) && $_GET['reset'] === 'true') {
    setcookie('sergioVotes', 0, time() - 3600);
    setcookie('yiderVotes', 0, time() - 3600);
    setcookie('franklinVotes', 0, time() - 3600);
    setcookie('blankVotes', 0, time() - 3600);
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}
?>
