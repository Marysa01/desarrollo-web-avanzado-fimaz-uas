<?php

class Usuario {

    // Atributos privados
    private $nombre;
    private $correo;

    // Constructor
    public function __construct($nombre, $correo) {
        $this->nombre = $nombre;
        $this->correo = $correo;
    }

    // Método getNombre()
    public function getNombre() {
        return $this->nombre;
    }

    // Método getCorreo()
    public function getCorreo() {
        return $this->correo;
    }

    // Método setNombre()
    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    // Método setCorreo()
    public function setCorreo($correo) {
        $this->correo = $correo;
    }
}

?>