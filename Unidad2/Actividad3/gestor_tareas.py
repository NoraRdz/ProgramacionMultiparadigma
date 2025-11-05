import json


class Tarea:
    def __init__(self, titulo, descripcion, prioridad="Normal"):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completada = False
        self.__prioridad = prioridad

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def completada(self):
        return self.__completada

    @property
    def prioridad(self):
        return self.__prioridad

    def marcar_completada(self):
        self.__completada = True

    def mostrar_info(self):
        estado = "Completada" if self.__completada else "Pendiente"
        return f"[{self.prioridad}] {self.titulo} - {self.descripcion} ({estado})"

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "prioridad": self.__prioridad,
            "completada": self.__completada
        }

    @classmethod
    def from_dict(cls, data):
        tipo = data.get("tipo", "Tarea")
        if tipo == "TareaUrgente":
            tarea = TareaUrgente(data["titulo"], data["descripcion"])
        elif tipo == "TareaRecurrente":
            tarea = TareaRecurrente(data["titulo"], data["descripcion"])
        else:
            tarea = Tarea(data["titulo"], data["descripcion"], data["prioridad"])
        if data.get("completada"):
            tarea.marcar_completada()
        return tarea


class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, prioridad="Urgente")

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base}"


class TareaRecurrente(Tarea):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, prioridad="Recurrente")

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base}"


class GestorTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, tarea):
        self.__tareas.append(tarea)

    def listar_tareas(self):
        if not self.__tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.__tareas, start=1):
                print(f"{i}. {tarea.mostrar_info()}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.__tareas):
            self.__tareas[indice].marcar_completada()
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.__tareas):
            eliminada = self.__tareas.pop(indice)
            print(f"Tarea '{eliminada.titulo}' eliminada.")
        else:
            print("Índice inválido.")

    def guardar_en_archivo(self, nombre_archivo="tareas.json"):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.__tareas], f, indent=4, ensure_ascii=False)
        print("Tareas guardadas correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="tareas.json"):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.__tareas = [Tarea.from_dict(d) for d in data]
            print("Tareas cargadas correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Se iniciará uno nuevo.")
