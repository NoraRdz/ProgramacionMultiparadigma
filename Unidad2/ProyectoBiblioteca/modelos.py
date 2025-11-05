# biblioteca/modelos.py

"""Módulo que define las clases principales y la lógica de negocio."""

class Libro:
    """Representa un libro en la biblioteca."""

    def __init__(self, titulo, autor, anio, estado="disponible"):
        """
        Inicializa un objeto Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            anio (int): El año de publicación del libro.
            estado (str): El estado del libro ('disponible' o 'prestado').
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado = estado

    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f'"{self.titulo}" por {self.autor} ({self.anio}) - {self.estado.capitalize()}'

    def to_dict(self):
        """Convierte el objeto Libro a un diccionario para serialización JSON."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "estado": self.estado,
        }


class Usuario:
    """Representa a un usuario de la biblioteca."""

    def __init__(self, nombre, libros_prestados=None):
        """
        Inicializa un objeto Usuario.

        Args:
            nombre (str): El nombre del usuario.
            libros_prestados (list, optional): Lista de títulos de libros prestados.
                                               Defaults to an empty list.
        """
        self.nombre = nombre
        self.libros_prestados = libros_prestados if libros_prestados is not None else []

    def __str__(self):
        """Devuelve una representación en cadena del usuario."""
        prestamos = ", ".join(self.libros_prestados) if self.libros_prestados else "Ninguno"
        return f"Usuario: {self.nombre} | Préstamos: {prestamos}"

    def to_dict(self):
        """Convierte el objeto Usuario a un diccionario para serialización JSON."""
        return {"nombre": self.nombre, "libros_prestados": self.libros_prestados}


class Biblioteca:
    """
    Administra las colecciones de libros y usuarios,
    y contiene la lógica de negocio principal.
    """

    def __init__(self, libros=None, usuarios=None):
        """
        Inicializa un objeto Biblioteca.

        Args:
            libros (list, optional): Una lista de objetos Libro. Defaults to None.
            usuarios (list, optional): Una lista de objetos Usuario. Defaults to None.
        """
        self.libros = libros if libros is not None else []
        self.usuarios = usuarios if usuarios is not None else []

    # --- Métodos de búsqueda (helpers internos) ---

    def buscar_usuario(self, nombre):
        """Busca un usuario por nombre (insensible a mayúsculas)."""
        return next((u for u in self.usuarios if u.nombre.lower() == nombre.lower()), None)

    def buscar_libro(self, titulo):
        """Busca un libro por título (insensible a mayúsculas)."""
        return next((l for l in self.libros if l.titulo.lower() == titulo.lower()), None)

    # --- Métodos de Lógica de Negocio ("Acciones") ---

    def agregar_libro(self, titulo, autor, anio):
        """Crea y agrega un nuevo libro al catálogo."""
        if self.buscar_libro(titulo):
            return f"Error: El libro '{titulo}' ya existe en el catálogo."
        
        nuevo_libro = Libro(titulo, autor, anio)
        self.libros.append(nuevo_libro)
        return f"\nLibro '{titulo}' agregado correctamente."

    def agregar_usuario(self, nombre):
        """Crea y agrega un nuevo usuario."""
        if self.buscar_usuario(nombre):
            return f"\nError: El usuario '{nombre}' ya existe."
        
        nuevo_usuario = Usuario(nombre)
        self.usuarios.append(nuevo_usuario)
        return f"\nUsuario '{nombre}' agregado correctamente."

    def mostrar_libros_disponibles(self):
        """Devuelve una lista de objetos Libro que están disponibles."""
        return [libro for libro in self.libros if libro.estado == "disponible"]

    def prestar_libro(self, nombre_usuario, titulo_libro):
        """
        Gestiona el préstamo de un libro a un usuario.
        Modifica el estado del libro y la lista del usuario.
        """
        usuario = self.buscar_usuario(nombre_usuario)
        if not usuario:
            return f"Error: Usuario '{nombre_usuario}' no encontrado."

        libro = self.buscar_libro(titulo_libro)
        if not libro:
            return f"Error: Libro '{titulo_libro}' no encontrado."

        if libro.estado == "prestado":
            return f"Error: El libro '{titulo_libro}' ya está prestado."

        # Realizar la acción
        libro.estado = "prestado"
        usuario.libros_prestados.append(libro.titulo)
        return f"\nÉxito: El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}."

    def devolver_libro(self, nombre_usuario, titulo_libro):
        """
        Gestiona la devolución de un libro.
        Modifica el estado del libro y la lista del usuario.
        """
        usuario = self.buscar_usuario(nombre_usuario)
        if not usuario:
            return f"Error: Usuario '{nombre_usuario}' no encontrado."

        # Verificamos si el usuario realmente tiene ese libro (insensible a mayúsculas)
        titulo_en_lista = next((t for t in usuario.libros_prestados if t.lower() == titulo_libro.lower()), None)
        
        if not titulo_en_lista:
            return f"Error: El usuario {usuario.nombre} no tiene prestado el libro '{titulo_libro}'."

        libro = self.buscar_libro(titulo_libro)
        if not libro:
            # Esto sería un error de integridad de datos, pero lo manejamos
            return f"Error: Libro '{titulo_libro}' no encontrado en el catálogo general."

        # Realizar la acción
        libro.estado = "disponible"
        usuario.libros_prestados.remove(titulo_en_lista) # Quitamos el título exacto que encontramos
        return f"\nÉxito: El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}."