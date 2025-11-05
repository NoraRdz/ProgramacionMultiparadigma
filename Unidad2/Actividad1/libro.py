class Libro:

    biblioteca = "Biblioteca Central"

    def __init__(self, titulo, autor, anio_publicacion):
     
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.prestado = False

    def prestar(self):
      
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya estaba prestado.")

    def devolver(self):
      
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_estado(self):
       
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Estado: {estado}")
        print(f"Biblioteca: {Libro.biblioteca}")
        print("-" * 40)
