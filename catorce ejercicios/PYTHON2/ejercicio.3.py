""""Escribir un algoritmo que, ingresada una calificación del 1 al 10, muestre por pantalla el
siguiente mensaje. Cuando la calificación sea de 7 o superior mostrar “APROBADO” y si no
obtuvo esa calificación mostrar “REPROBADO”."""


num1 = int (input("Ingresa tu nota: "))

def comparar_notas(num1):

    if num1 == 0 or num1 > 10:
        print ("Datos incorrectos")
    elif num1 <= 6:
        return "Usted Reprobo"
    elif num1 >= 7:
        return "Usted Aprobo"
        

resultado = comparar_notas(num1)
print (resultado)