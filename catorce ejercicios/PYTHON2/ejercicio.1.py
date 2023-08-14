#Leer dos números, determinar cuál es el mayor de los dos y mostrar ese número en pantalla con el mensaje “Es el número mayor”.

numero_y = int(input("Escribe el primer numero: "))
numero_z = int (input("Escribe el segundo numero: "))

def comparar_numeros(y, z):
    if y > z: 
        return "El primer numero es MAYOR"
    elif y < z:
        return "El segundo numero es MAYOR"
    else: 
        return "Ambos numeros son iguales...."\

resultado = comparar_numeros(numero_y, numero_z)
print(resultado)