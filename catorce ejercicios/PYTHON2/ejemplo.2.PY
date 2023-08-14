#Dadas las tres calificaciones de un estudiante en la materia de algoritmia, calcule:
#a. Determinar su promedio
#b. Indicar si el estudiante aprobó o no el curso.
#Un estudiante aprueba la materia si el promedio es mayor o igual a 70 puntos.

print("Ejemplo 2")


nota1 = int (input("Escribe tu primer nota: "))
nota2 = int (input("Escribe tu segunda nota: "))
nota3 = int (input("Escribe tu tercer nota: "))


suma = (nota1+nota2+nota3)/3

if suma > 70:
    print ("usted aprobo",suma)
    
elif suma <70:
    print ("Usted reprobo",suma)
