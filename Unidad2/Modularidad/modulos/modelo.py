"""
Módulo que contiene la clase principal del sistema de inventario.
"""


class Producto:
    """
    Representa un producto en el inventario.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad disponible en inventario.
    """

    def __init__(self, nombre, precio, cantidad):
        """Inicializa un nuevo producto con nombre, precio y cantidad."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Devuelve una representación legible del producto."""
        return f"{self.nombre} - ${self.precio:.2f} ({self.cantidad} unidades)"
