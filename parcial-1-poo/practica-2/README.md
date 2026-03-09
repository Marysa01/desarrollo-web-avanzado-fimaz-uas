# PRÁCTICA DE LABORATORIO 2: HERENCIA Y REUTILIZACIÓN DE CÓDIGO EN PHP

## Explicación de la herencia aplicada

En esta práctica se aplicó el concepto de herencia en programación orientada a objetos.
Se creó una clase llamada **Admin** que hereda de la clase **Usuario** utilizando la palabra `extends`.
Gracias a esto, la clase Admin puede usar los atributos y métodos que ya están definidos en Usuario, como el nombre, el correo y los métodos getters y setters.
Además, se agregó un método propio llamado `getRol()` que devuelve el rol de Administrador.

## Diferencias entre Usuario y Admin

La clase **Usuario** es la clase base y contiene los atributos `nombre` y `correo`, así como los métodos para obtener y modificar esos valores.

La clase **Admin** es una clase que hereda de Usuario, por lo que reutiliza su funcionalidad. La diferencia es que Admin agrega un método adicional llamado `getRol()` que retorna el rol de administrador.

## Evidencia de ejecución

Para probar el funcionamiento se creó un objeto de tipo **Admin** en el archivo `index.php`.
Después se mostraron en el navegador el nombre, el correo y el rol utilizando los métodos correspondientes.

Al ejecutar el proyecto se muestra algo similar a lo siguiente:

Nombre: Maria
Correo: [maria@gmail.com]
Rol: Administrador
