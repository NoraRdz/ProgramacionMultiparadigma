# biblioteca/operaciones.py

"""Módulo para la persistencia de datos (guardar y cargar en JSON)."""

import json
from modelos import Libro, Usuario, Biblioteca

def guardar_datos(biblioteca, archivo="datos.json"):
    """
    Guarda el estado actual de la biblioteca en un archivo JSON.

    Args:
        biblioteca (Biblioteca): El objeto Biblioteca a guardar.
        archivo (str): La ruta del archivo donde se guardarán los datos.
    """
    datos = {
        "libros": [libro.to_dict() for libro in biblioteca.libros],
        "usuarios": [usuario.to_dict() for usuario in biblioteca.usuarios],
    }
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Datos guardados exitosamente.")
    except IOError as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos(archivo="datos.json"):
    """
    Carga los datos de la biblioteca desde un archivo JSON.

    Args:
        archivo (str): La ruta del archivo desde donde se cargarán los datos.

    Returns:
        Biblioteca: Un objeto Biblioteca con los datos cargados.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            libros = [Libro(**libro_data) for libro_data in datos.get("libros", [])]
            usuarios = [Usuario(**usuario_data) for usuario_data in datos.get("usuarios", [])]
            print("Datos cargados exitosamente.")
            return Biblioteca(libros, usuarios)
    except FileNotFoundError:
        print("Archivo de datos no encontrado. Empezando con una biblioteca vacía.")
        return Biblioteca()
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Empezando con una biblioteca vacía.")
        return Biblioteca()
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar los datos: {e}")
        return Biblioteca()