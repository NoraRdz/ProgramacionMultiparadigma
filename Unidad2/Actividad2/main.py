from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\n===== MENÚ DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar precio")
    print("5. Modificar stock")
    print("6. Mostrar valor total del inventario")
    print("7. Comparar dos productos")
    print("8. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad inicial: "))
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")
                continue

            try:
                nuevo = Producto(nombre, precio)
                inventario.agregar_producto(nuevo, cantidad)
                print(f"Producto '{nombre}' agregado correctamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print("\n=== INVENTARIO ===")
            print(inventario)

        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Producto a modificar precio: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    producto.precio = nuevo_precio
                    print(f"Precio actualizado a ${nuevo_precio:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            nombre = input("Producto a modificar stock: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                try:
                    nuevo_stock = int(input("Nuevo stock: "))
                    producto.stock = nuevo_stock
                    print(f"Stock actualizado a {nuevo_stock}.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            total = inventario.total_valor_inventario()
            print(f"Valor total del inventario: ${total:.2f}")

        elif opcion == "7":
            nombre1 = input("Nombre del primer producto: ")
            nombre2 = input("Nombre del segundo producto: ")

            p1 = inventario.buscar_producto(nombr_
