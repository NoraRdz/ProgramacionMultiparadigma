"""
Módulo con funciones auxiliares del sistema de inventario.
"""


def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción seleccionada por el usuario.

    Retorna:
        str: Opción elegida.
    """
    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    return input("Selecciona una opción: ")
