#Diseñe un algoritmo que dado dos números A y B, determine si A es mayor, igual o menor a B.
print ("Ejemplo 3")

numero_a = int(input("Ingrese el valor de A: "))
numero_b = int(input("Ingrese el valor de B: "))

def comparar_numeros(a, b):
    if a > b:
        return "A es mayor que B"
    elif a < b:
        return "A es menor que B"
    else:
        return "A es igual a B"
        
resultado = comparar_numeros(numero_a, numero_b)
print(resultado)