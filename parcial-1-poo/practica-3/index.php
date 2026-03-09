<?php

require_once "clases/Admin.php";
require_once "clases/Alumno.php";

try {

    // Usuario administrador válido
    $admin = new Admin("Maria", "maria@gmail.com");

    echo "Nombre: " . $admin->getNombre() . "<br>";
    echo "Correo: " . $admin->getCorreo() . "<br>";
    echo "Rol: " . $admin->getRol() . "<br><br>";

    // Alumno válido
    $alumno = new Alumno("Juan", "juan@gmail.com", "A12345");

    echo "Nombre: " . $alumno->getNombre() . "<br>";
    echo "Correo: " . $alumno->getCorreo() . "<br>";
    echo "Matrícula: " . $alumno->getMatricula() . "<br>";
    echo "Rol: " . $alumno->getRol() . "<br><br>";

    // Usuario inválido (correo incorrecto)
    $usuarioError = new Usuario("Pedro", "correo_invalido");

} catch (Exception $e) {

    echo "Error: " . $e->getMessage();

}

?>