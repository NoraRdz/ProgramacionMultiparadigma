from producto import Producto


class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto: Producto, cantidad: int = 0):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        if producto.nombre in self.__productos:
            existente = self.__productos[producto.nombre]
            existente.stock += cantidad
        else:
            producto.stock = cantidad
            self.__productos[producto.nombre] = producto

    def buscar_producto(self, nombre: str):
        return self.__productos.get(nombre)

    def total_valor_inventario(self):
        total = sum(p.precio * p.stock for p in self.__productos.values())
        return total

    def __len__(self):
        return len(self.__productos)

    def __str__(self):
        if not self.__productos:
            return "El inventario está vacío."
        return "\n".join(str(p) for p in self.__productos.values())
