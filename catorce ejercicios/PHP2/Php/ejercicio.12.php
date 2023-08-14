<!-- Realizar un login de usuario, solicitando el correo y la contraseña, 
si el correo=’fund@gmail.com’ y la clave=’123456‘, el sistema mostrará el mensaje 
“Bienvenidos a Fundamentos de programación”, si los datos son inválidos el sistema deberá 
mostrar “Error en los datos de ingreso.”  -->
<form method="post">
        <label for="email">Correo:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit" name="login">Iniciar Sesión</button>
    </form>
    <?php
    if (isset($_POST['login'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];

        if ($email === 'f@gmail.com' && $password === '123456') {
            echo "<script>alert('Bienvenidos a Fundamentos de programación');</script>";
        } else {
            echo "<script>alert('Error en los datos de ingreso');</script>";
        }
    }
    ?>