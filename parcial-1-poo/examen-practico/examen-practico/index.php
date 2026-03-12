<?php

require_once "clases/Admin.php";
require_once "clases/Alumno.php";

$usuarios = [];

try {

    $admin = new Admin("Marysa Quiñonez Chavez", "marysaq1@uas.edu.mx.com");
    $usuarios[] = $admin;

    $alumno = new Alumno("Ana Perez Ortiz", "anap@gmail.com", "A12345");
    $usuarios[] = $alumno;

    $error = new Alumno("Luis Alvarado", "luis45.uas.edu.mx", "A99999");
    $usuarios[] = $error;

} catch (Exception $e) {

    $mensajeError = $e->getMessage();

}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Sistema de Usuarios</title>
</head>
<body>

<h2>Lista de Usuarios</h2>

<table border="1">
<tr>
<th>Nombre</th>
<th>Correo</th>
<th>Rol</th>
<th>Matricula</th>
</tr>

<?php foreach ($usuarios as $u): ?>

<tr>
<td><?php echo $u->getNombre(); ?></td>
<td><?php echo $u->getCorreo(); ?></td>
<td><?php echo $u->getRol(); ?></td>

<td>
<?php
if ($u instanceof Alumno) {
    echo $u->getMatricula();
} else {
    echo "—";
}
?>
</td>

</tr>

<?php endforeach; ?>

</table>

<?php
if (isset($mensajeError)) {
    echo "<p style='color:red;'>Error controlado: $mensajeError</p>";
}
?>

</body>
</html>