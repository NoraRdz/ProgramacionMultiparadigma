"""
Módulo principal del sistema de inventario.

Controla el flujo del programa y permite al usuario interactuar
con las funciones de los demás módulos.
"""

from modulos.operaciones import agregar_producto, listar_productos, eliminar_producto, buscar_producto
from modulos.utilidades import mostrar_menu


def main():
    """Función principal del programa. Muestra el menú y gestiona las acciones del usuario."""
    inventario = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            listar_productos(inventario)

        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, nombre)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "5":
            print("Saliendo del sistema de inventario...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
