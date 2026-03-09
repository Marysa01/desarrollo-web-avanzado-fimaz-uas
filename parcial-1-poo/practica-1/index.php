<?php

// 1. Incluir el archivo Usuario.php
require_once "Usuario.php";

// 2. Crear una instancia de la clase Usuario
$usuario = new Usuario("María", "maria@gmail.com");

// 3. Mostrar los valores utilizando los métodos getters
echo "Nombre: " . $usuario->getNombre() . "<br>";
echo "Correo: " . $usuario->getCorreo();

?>