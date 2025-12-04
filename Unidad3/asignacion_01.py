def crear_transformador(funcion):
    """
    Recibe una función y retorna otra función que aplica
    esa transformación a cada elemento de una lista (similar a map).
    """
    def transformador(lista):
        return [funcion(item) for item in lista]
    return transformador

def crear_filtro(predicado):
    """
    Recibe un predicado y retorna una función que filtra
    una lista dejando solo elementos que lo cumplen (similar a filter).
    """
    def filtro(lista):
        return [item for item in lista if predicado(item)]
    return filtro

def crear_reductor(funcion, valor_inicial):
    """
    Recibe una función de reducción y un valor inicial,
    retorna una función que reduce una lista a un solo valor (similar a reduce).
    """
    def reductor(lista):
        acumulador = valor_inicial
        for item in lista:
            acumulador = funcion(acumulador, item)
        return acumulador
    return reductor

def componer(*funciones):
    """
    Recibe múltiples funciones y retorna una nueva función
    que las aplica en secuencia (de izquierda a derecha).
    """
    def pipeline(data):
        resultado = data
        for func in funciones:
            resultado = func(resultado)
        return resultado
    return pipeline

# --- SECCIÓN DE PRUEBAS (Según la imagen) ---

if __name__ == "__main__":
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]
    
    pipeline = componer(
        crear_filtro(lambda x: x > 0),
        crear_transformador(lambda x: x ** 2),
        crear_reductor(lambda acc, x: acc + x, 0)
    )

    resultado = pipeline(numeros)
    
    print(f"Resultado: {resultado}") 
    # Lógica esperada:
    # Positivos: [1, 3, 5, 7, 8, 10]
    # Cuadrados: [1, 9, 25, 49, 64, 100]
    # Suma: 1 + 9 + 25 + 49 + 64 + 100 = 248