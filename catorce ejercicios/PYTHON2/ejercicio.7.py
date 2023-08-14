"""A un trabajador le descuentan de su sueldo el 12% si su sueldo es menor o igual a 500000, por
encima de 500000 y hasta 1000000 el 15%, y por encima de 1000000 el 18%. Realice un
algoritmo que calcule el descuento y sueldo total que recibe el trabajador dado su sueldo
inicial."""

sueldo = int(input("Ingrese su sueldo: "))

if sueldo <= 500000 and sueldo > 0:
    total1 = sueldo - (sueldo*0.12)
    print("El sueldo total que recibira sera de: $",int(total1))
elif sueldo <= 0:
    print("Sueldo no valido")
elif sueldo >= 500000 and sueldo < 1000000:
    total2 = sueldo - (sueldo*0.15)
    print("El sueldo total que recibira sera de: $",int(total2))
elif sueldo >= 1000000:
    total3 = sueldo - (sueldo*0.18)
    print("El sueldo total que recibira sera de: $",int(total3))