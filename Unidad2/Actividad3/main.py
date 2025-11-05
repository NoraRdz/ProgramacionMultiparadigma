from gestor_tareas import GestorTareas, Tarea, TareaUrgente, TareaRecurrente

def menu():
    gestor = GestorTareas()
    gestor.cargar_desde_archivo()

    while True:
        print("\n=== MENÚ DE GESTIÓN DE TAREAS ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Guardar y salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            print("Tipo de tarea:")
            print("1. Normal")
            print("2. Urgente")
            print("3. Recurrente")
            tipo = input("Selecciona: ")
            if tipo == "2":
                tarea = TareaUrgente(titulo, descripcion)
            elif tipo == "3":
                tarea = TareaRecurrente(titulo, descripcion)
            else:
                tarea = Tarea(titulo, descripcion)
            gestor.agregar_tarea(tarea)
            print("Tarea agregada correctamente.")

        elif opcion == "2":
            gestor.listar_tareas()

        elif opcion == "3":
            gestor.listar_tareas()
            indice = int(input("Número de tarea a marcar: ")) - 1
            gestor.marcar_completada(indice)

        elif opcion == "4":
            gestor.listar_tareas()
            indice = int(input("Número de tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(indice)

        elif opcion == "5":
            gestor.guardar_en_archivo()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
