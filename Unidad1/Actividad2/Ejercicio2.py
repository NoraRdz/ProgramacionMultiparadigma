score=int(input("Calificacion: "))

if score>100:
    print("La calificacion no puede ser más de 100")
elif score >=90:
    print("Calificacion: A")
elif score>=80 :
    print("Calificacion: B")
elif score>=70:
    print("Calificacion: C")
elif score>=90:
    print("Calificacion: D")
else:
    print("Calificacion: F")