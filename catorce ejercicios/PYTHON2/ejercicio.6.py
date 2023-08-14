"""Hacer un algoritmo para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe
que, si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas
entonces las horas extras se le pagarán a $25 por hora."""

trabajo = input("Ingrese las horas de trabajo: ")

if not trabajo.isdigit():
    print("Error, datos no válidos")
else:
    trabajo = int(trabajo)
    if trabajo < 0:
        print("Error, datos no válidos")
    elif trabajo <= 40:
        total = trabajo * 20
        print("Su sueldo para esta semana será de:", total, "dólares")
    elif trabajo > 40:
        total1 = trabajo * 25
        print("Su sueldo para esta semana será de:", total1, "dólares")
