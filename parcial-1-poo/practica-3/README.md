# PRÁCTICA DE LABORATORIO 3: SISTEMA DE USUARIOS CON VALIDACIONES Y EXCEPCIONES

## Descripción del sistema

En esta práctica se desarrolló un pequeño sistema de usuarios utilizando programación orientada a objetos en PHP. El sistema permite crear distintos tipos de usuarios como administradores y alumnos.
Además, se implementó una validación para verificar que el correo electrónico tenga un formato correcto. En caso de que el correo no sea válido, se genera una excepción para evitar que el programa continúe con datos incorrectos.

## Explicación del flujo de clases

La clase principal es **Usuario**, que contiene los atributos `nombre` y `correo`. En esta clase también se realiza la validación del correo utilizando una función que revisa si el formato es correcto.

A partir de esta clase se crean dos clases derivadas:

* **Admin**: hereda de Usuario y tiene un método `getRol()` que retorna "Administrador".
* **Alumno**: también hereda de Usuario y agrega un atributo adicional llamado `matricula`, además de un método `getRol()` que retorna "Alumno".

En el archivo `index.php` se incluyen las clases, se crean algunos objetos y se muestran los datos en el navegador.

## Evidencia del manejo de errores

Para controlar errores se utilizó un bloque `try/catch`.
Dentro del `try` se intenta crear usuarios válidos y también un usuario con un correo incorrecto. Cuando el correo no cumple con el formato requerido, se lanza una excepción y el bloque `catch` muestra un mensaje de error controlado.

Esto permite que el programa no se detenga abruptamente y que el error sea mostrado de forma clara al usuario.
