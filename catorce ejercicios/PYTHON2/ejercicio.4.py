"""En un estacionamiento cobran $1.500 por hora. Diseñe un algoritmo que determine cuanto
debe pagar un cliente por el estacionamiento de su vehículo, conociendo el tiempo de
estacionamiento en horas."""

num1 = int(input("Ingrese el tiempo de estacionamiento en horas: "))


def pago_estacionamiento(num1):
    costo = 1500
    total = costo * num1
    return total

estacionamiento = pago_estacionamiento(num1)
print("El cliente debe pagar:", estacionamiento, "pesos")