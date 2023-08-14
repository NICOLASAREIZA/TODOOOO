"""Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se desea calcular el
jornal diario de acuerdo con los siguientes puntos:
La tarifa de las horas diurnas es de 10 dólares.
La tarifa de las horas nocturnas es de 15 dólares.
Codifique un algoritmo que solicite el turno de trabajo y el número de horas trabajadas y
posteriormente calcule el valor a pagar."""


turno = input ("Ingrese su turno de trabajo (Diurno o Nocturno): ")
horas = int(input ("Ingrese las horas: "))

turno = turno.lower()
if turno == "diurno":
    resultado = horas * 10
    print ("El valor a pagar es de: ",resultado," dolares")
elif turno == "nocturno":
    resultado2 = horas * 15
    print ("El valor a pagar es de:",resultado2, " dolares")
else:
    print("ERROR")

