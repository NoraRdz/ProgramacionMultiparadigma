"""
Módulo con funciones que gestionan las operaciones del inventario.
"""

from modulos.modelo import Producto


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad del producto.
    """
    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)
    print(f"✅ Producto '{nombre}' agregado correctamente.")


def listar_productos(inventario):
    """
    Muestra todos los productos registrados en el inventario.

    Parámetros:
        inventario (list): Lista de productos.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nLista de productos:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto}")
        print()


def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre y muestra sus detalles.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a buscar.
    """
    for producto in inventario:
        if producto.nombre.lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            return
    print("Producto no encontrado.")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por su nombre.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a eliminar.
    """
    for producto in inventario:
        if producto.nombre.lower() == nombre.lower():
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
    print("No se encontró el producto especificado.")
