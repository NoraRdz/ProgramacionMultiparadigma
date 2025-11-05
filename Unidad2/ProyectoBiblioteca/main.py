# biblioteca/main.py

"""
Programa principal (Interfaz de Usuario) para interactuar con el
sistema de gestión de la biblioteca.
"""

# Importamos las funciones de persistencia
import operaciones as persistencia

# Importamos la clase principal que contiene la lógica
from modelos import Biblioteca

def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar un nuevo libro")
    print("2. Agregar un nuevo usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Salir y guardar")
    print("---------------------------------------")

def main():
    """Función principal que ejecuta el bucle del programa."""
    
    # 1. Cargar datos
    # 'mi_biblioteca' es la instancia principal que contiene el estado
    mi_biblioteca = persistencia.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Pedimos datos al usuario
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            while True:
                try:
                    anio = int(input("Ingrese el año de publicación: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un año válido.")
            
            # Llamamos al método de la biblioteca
            resultado = mi_biblioteca.agregar_libro(titulo, autor, anio)
            print(resultado)

        elif opcion == "2":
            # Pedimos datos al usuario
            nombre = input("Ingrese el nombre del nuevo usuario: ")
            
            # Llamamos al método de la biblioteca
            resultado = mi_biblioteca.agregar_usuario(nombre)
            print(resultado)

        elif opcion == "3":
            # Llamamos al método
            libros_disponibles = mi_biblioteca.mostrar_libros_disponibles()
            
            if not libros_disponibles:
                print("\nNo hay libros disponibles en este momento.")
            else:
                print("\n--- Libros Disponibles ---")
                for libro in libros_disponibles:
                    # Usamos el __str__ del objeto Libro
                    print(f"- {libro}") 
                print("--------------------------")

        elif opcion == "4":
            # Pedimos datos
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            titulo_libro = input("Ingrese el título del libro a prestar: ")
            
            # Llamamos al método
            resultado = mi_biblioteca.prestar_libro(nombre_usuario, titulo_libro)
            print(resultado)

        elif opcion == "5":
            # Pedimos datos
            nombre_usuario = input("Ingrese el nombre del usuario que devuelve: ")
            titulo_libro = input("Ingrese el título del libro a devolver: ")
            
            # Llamamos al método
            resultado = mi_biblioteca.devolver_libro(nombre_usuario, titulo_libro)
            print(resultado)

        elif opcion == "6":
            # 6. Guardar datos al salir
            persistencia.guardar_datos(mi_biblioteca)
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()