def main():
    menu = 0  # Inicializar la variable
    while menu != 3:
        menu = int(input("Elige qué quieres hacer: \n1. Suma\n2. Resta\n3. Salir\nOpción: "))
        resultado = 0
        if menu == 1:
            resultado = Suma()
            print(f"El resultado de la suma es {resultado}")
        elif menu == 2:
            resultado = Resta()
            print(f"El resultado de la resta es {resultado}")
        elif menu == 3:
            print("Saliendo...")
        else:
            print("Opción no válida")

def Suma():
    print("Has elegido suma")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1 + num2

def Resta():
    print("Has elegido resta")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1 - num2

if __name__ == "__main__":
    main()