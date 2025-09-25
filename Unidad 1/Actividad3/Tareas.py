def main():
    tareas = []

    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            AgregarTarea(tareas)
        elif opcion == "2":
            MostrarTareas(tareas)
        elif opcion == "3":
            ActualizarTarea(tareas)
        elif opcion == "4":
            EliminarTarea(tareas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


def AgregarTarea(tareas):
    titulo = input("Escribe la nueva tarea: ")
    tarea = {"titulo": titulo, "estado": "pendiente"}
    tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada con estado pendiente.")


def MostrarTareas(tareas):
    tareas_visibles = [t for t in tareas if t["estado"] != "cancelado"]

    if not tareas_visibles:
        print("No hay tareas pendientes o activas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas_visibles, start=1):
            print(f"{i}. {tarea['titulo']} - Estado: {tarea['estado']}")


def ActualizarTarea(tareas):
    tareas_visibles = [t for t in tareas if t["estado"] != "cancelado"]

    if not tareas_visibles:
        print("No hay tareas para actualizar.")
        return

    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas_visibles, start=1):
        print(f"{i}. {tarea['titulo']} - Estado: {tarea['estado']}")

    try:
        seleccion = int(input("Selecciona el número de la tarea a actualizar (0 para salir): "))
        if seleccion == 0:
            return
        if 1 <= seleccion <= len(tareas_visibles):
            tarea = tareas_visibles[seleccion - 1]
            print("Estados disponibles: pendiente, finalizado, pausado")
            nuevo_estado = input("Nuevo estado: ").strip().lower()
            if nuevo_estado in ["pendiente", "finalizado", "pausado"]:
                tarea["estado"] = nuevo_estado
                print(f"Tarea '{tarea['titulo']}' actualizada a estado '{nuevo_estado}'.")
            else:
                print("Estado no válido.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingresa un número válido.")


def EliminarTarea(tareas):
    tareas_visibles = [t for t in tareas if t["estado"] != "cancelado"]

    if not tareas_visibles:
        print("No hay tareas para eliminar.")
        return

    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas_visibles, start=1):
        print(f"{i}. {tarea['titulo']} - Estado: {tarea['estado']}")

    try:
        seleccion = int(input("Selecciona el número de la tarea a eliminar (0 para salir): "))
        if seleccion == 0:
            return
        if 1 <= seleccion <= len(tareas_visibles):
            tarea = tareas_visibles[seleccion - 1]
            tarea["estado"] = "cancelado"
            print(f"Tarea '{tarea['titulo']}' ha sido marcada como cancelada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingresa un número válido.")


if __name__ == "__main__":
    main()
