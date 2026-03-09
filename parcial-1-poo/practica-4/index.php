<?php

require_once "clases/Admin.php";
require_once "clases/Alumno.php";
require_once "clases/Invitado.php";

$usuarios = [];

try {

    // Usuarios válidos
    $usuarios[] = new Admin("Maria", "maria@gmail.com");
    $usuarios[] = new Alumno("Juan", "juan@gmail.com", "A12345");
    $usuarios[] = new Invitado("Ana", "ana@gmail.com", "Empresa XYZ");

    // Usuario con correo inválido
    $usuarios[] = new Admin("Pedro", "correo_invalido");

} catch (Exception $e) {

    echo "<p style='color:red;'>Error controlado: " . $e->getMessage() . "</p>";

}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Sistema de Usuarios</title>
</head>
<body>

<h2>Lista de Usuarios</h2>

<table border="1" cellpadding="8">
<tr>
<th>Nombre</th>
<th>Correo</th>
<th>Rol</th>
<th>Matrícula</th>
<th>Empresa</th>
</tr>

<?php

foreach ($usuarios as $u){

    $matricula = "—";
    $empresa = "—";

    if($u instanceof Alumno){
        $matricula = $u->getMatricula();
    }

    if($u instanceof Invitado){
        $empresa = $u->getEmpresa();
    }

    echo "<tr>";
    echo "<td>".$u->getNombre()."</td>";
    echo "<td>".$u->getCorreo()."</td>";
    echo "<td>".$u->getRol()."</td>";
    echo "<td>".$matricula."</td>";
    echo "<td>".$empresa."</td>";
    echo "</tr>";
}

?>

</table>

</body>
</html>