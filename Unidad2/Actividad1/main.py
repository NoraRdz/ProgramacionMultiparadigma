from libro import Libro

libros = []


def registrar_libro():
    print("\n=== Registrar nuevo libro ===")
    titulo = input("Título: ")
    autor = input("Autor: ")
    try:
        anio = int(input("Año de publicación: "))
    except ValueError:
        print("El año debe ser un número.")
        return

    nuevo_libro = Libro(titulo, autor, anio)
    libros.append(nuevo_libro)
    print(f"Libro '{titulo}' registrado correctamente.")


def mostrar_libros():
    print("\n=== Lista de libros ===")
    if not libros:
        print("No hay libros registrados.")
        return
    for i, libro in enumerate(libros, start=1):
        print(f"{i}. {libro.titulo} ({'Prestado' if libro.prestado else 'Disponible'})")


def prestar_libro():
    mostrar_libros()
    if not libros:
        return
    try:
        indice = int(input("\nNúmero del libro a prestar: ")) - 1
        libros[indice].prestar()
    except (ValueError, IndexError):
        print("Selección inválida.")


def devolver_libro():
    mostrar_libros()
    if not libros:
        return
    try:
        indice = int(input("\nNúmero del libro a devolver: ")) - 1
        libros[indice].devolver()
    except (ValueError, IndexError):
        print("Selección inválida.")


def mostrar_detalles():
    print("\n=== Detalles de todos los libros ===")
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        libro.mostrar_estado()


def menu():
    while True:
        print("\n===== MENÚ DE BIBLIOTECA =====")
        print("1. Registrar nuevo libro")
        print("2. Mostrar lista de libros")
        print("3. Prestar un libro")
        print("4. Devolver un libro")
        print("5. Mostrar detalles de todos los libros")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            mostrar_detalles()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
