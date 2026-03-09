# PRÁCTICA DE LABORATORIO 4: INTEGRACIÓN POO + HERENCIA + VALIDACIONES + EXCEPCIONES (PHP 8+)

## Objetivo de la práctica

El objetivo de esta práctica es aplicar varios conceptos de programación orientada a objetos en PHP, como encapsulamiento, herencia y polimorfismo.
También se implementa validación de datos y manejo de excepciones para evitar errores en el sistema.
Finalmente, se muestran los resultados en una tabla HTML.

## Requisitos

Para ejecutar esta práctica se necesita:

* PHP 8 o superior
* Servidor local (por ejemplo XAMPP)
* Navegador web
* Los archivos del proyecto dentro de la carpeta `htdocs`

## Ruta de ejecución en el navegador

Una vez que el proyecto esté dentro del servidor local, se puede abrir en el navegador con una ruta similar a la siguiente:

http://localhost/desarrollo-web-avanzado-fimaz-uas/parcial-1-poo/practica-4/

## Evidencia esperada

Al ejecutar el sistema se debe mostrar:

* Una tabla HTML con los usuarios válidos creados (Administrador, Alumno e Invitado).
* Cada usuario debe mostrar su nombre, correo y rol correspondiente.
* En las columnas que no aplican (matrícula o empresa) se muestra el símbolo "—".
* Cuando se intenta crear un usuario con un correo inválido, el sistema muestra un mensaje de error controlado utilizando manejo de excepciones.
