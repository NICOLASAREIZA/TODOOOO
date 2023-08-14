# Realizar un programa que capture los datos de un empleado:
# Nombre, Genero (1-masculino, 2-femenino), Salario básico, y tiempo de servicio.
# El sistema debe calcular el valor de la bonificación anual en base a los siguientes
# lineamientos de la empresa:
# Si es mujer y el tiempo de servicio es superior a 5 años, su bonificación será de un 20% del
# Salario básico
# Si es mujer y el tiempo de servicio es inferior o igual a 5 años, su bonificación será de un
# 15% del Salario básico
# Si es hombre y el tiempo de servicio es superior a 6 años, su bonificación será de un 20% del
# Salario Básico.
# Si es hombre y el tiempo de servicio está entre 1 y 6 años su bonificación será de un 15%
# del Salario Básico.

def calcular_bonificacion(nombre, genero, salario, servicio):
    resultado = ""
    if salario < 0 or servicio < 0:
        resultado = "Error, datos no válidos"
    else:
        if genero == 2 and servicio > 5:
            bonificacion = salario * 0.20
            resultado = f"Bonificación 20%: {bonificacion}, Total {salario + bonificacion}"
        elif genero == 2 and servicio <= 5:
            bonificacion = salario * 0.15
            resultado = f"Bonificación 15%: {bonificacion}, Total {salario + bonificacion}"
        elif genero == 1 and servicio > 6:
            bonificacion = salario * 0.20
            resultado = f"Bonificación 20%: {bonificacion}, Total {salario + bonificacion}"
        elif genero == 1 and 1 < servicio <= 6:
            bonificacion = salario * 0.15
            resultado = f"Bonificación 15%: {bonificacion}, Total {salario + bonificacion}"
        elif genero == 3:
            bonificacion = salario * 0.10
            resultado = f"Bonificación 10%: {bonificacion}, Total {salario + bonificacion}"
    
    return resultado

nombre = input("Ingrese el nombre: ")
genero = int(input("Ingrese el género (1: Masculino, 2: Femenino, 3: Otro): "))
salario = float(input("Ingrese el salario: "))
servicio = float(input("Ingrese los años de servicio: "))

resultado = calcular_bonificacion(nombre, genero, salario, servicio)
print(resultado)