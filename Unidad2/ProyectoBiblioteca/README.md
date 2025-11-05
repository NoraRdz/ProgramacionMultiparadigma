Descripción

Aplicación de consola que simula un sistema sencillo de gestión de biblioteca. Permite agregar libros y usuarios, listar libros disponibles, prestar y devolver libros, y persistir los datos en un archivo biblioteca_datos.json.

El proyecto está diseñado para demostrar:

Uso de clases, encapsulación y relaciones entre objetos.

Herencia y polimorfismo (clase base Recurso y subclase Libro).

Modularidad (módulos separados para modelos, operaciones y persistencia).

Documentación con docstrings y estilo PEP 8 / PEP 257.

Requisitos

Python 3.8+

Cómo ejecutar

Clonar el repositorio.

Abrir una terminal en la carpeta biblioteca.

Ejecutar:

python main.py

Se iniciará un menú interactivo en consola.

Estructura del código

modelos.py — Define las clases Recurso, Libro, Usuario y Biblioteca.

operaciones.py — Funciones que implementan la lógica de añadir, listar, prestar y devolver.

datos.py — Persistencia: guardar y cargar a JSON.

main.py — Interfaz de consola (menú) que usa los módulos anteriores.

Posibles temas alternativos

Sistema de gestión de pedidos en una tienda.

Control de estudiantes y calificaciones.

Sistema de inventario.

Gestor de tareas o eventos personales.

Simulación de cuentas bancarias.