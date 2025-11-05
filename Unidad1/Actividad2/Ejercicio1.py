def main():
    menu = int(input("Elige de qué figura quieres calcular el área: \n1. Cuadrado\n2. Círculo\n3. Triángulo\nOpción: "))
    resultado=0
    seleccion=""
    if(menu==1):
        resultado=Area_Cuadrado()
        seleccion="cuadrado"
    elif(menu==2):
        resultado=Area_Circulo()
        seleccion="circulo"
    elif(menu==3):
        resultado=Area_Triangulo()
        seleccion="triangulo"
    
    print(f"El resultado del area de {seleccion} es {resultado}")




def Area_Cuadrado():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la Altura: "))
    resultado=base*altura
    
    return resultado


def Area_Circulo():
    radio=float(input("Ingrese el valor de radio del circulo: "))
    resultado=3.16*(radio**2)
    return resultado

def Area_Triangulo():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la Altura: "))
    resultado=(base*altura)/2
    
    return resultado

if __name__=="__main__":
    main()