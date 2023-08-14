#Diseñar un algoritmo que dada la edad de una persona indique si es MAYOR o MENOR de edad.


print("Ejemplo 1")

edad = int (input ("Ingrese su edad, por favor: "))

if edad == 0 or edad > 100:
    print ("Edad incorrecta")
        
elif edad >= 18:
    print ("Usted es mayor de edad ",edad)

elif edad <= 17:
    print ("Usted es menor de edad ",edad)