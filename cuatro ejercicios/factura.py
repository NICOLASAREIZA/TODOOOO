""""Una empresa de insumos agrícolas esta de promoción por el día de hoy y ofrece un
descuente del 17.5% por las compras realizadas. Elaborar un script donde muestre la
factura de venta con el descuento con la siguiente información:

Ciudad y Fecha:
Nombre del cliente:
Nombre del producto:
Valor del producto:
Cantidad del producto:
Valor total:
Valor del descuento:
Valor total con descuento: """


print("Ingresa nombre de la ciudad:")
ciudad = input()
print("Ingresa la fecha:")
fecha = input()
print("Ingresa el nombre del producto:")
producto = input()
print("Ingresa el nombre del cliente:")
cliente = input()

try:
    print("Ingresa la cantidad de productos:")
    cantidad = int(input())
    print("Ingresa el valor del producto:")
    valor = float(input())
    
    if cantidad > 0 and valor > 0:
        valortotal = valor * cantidad
        descuento = valortotal * 0.175
        valordescuento = valortotal - descuento

        print("Ciudad en la que reside:", ciudad)
        print("Fecha de factura:", fecha)
        print("Nombre del producto:", producto)
        print("Nombre del cliente:", cliente)
        print("Valor del producto: $", valor)
        print("Cantidad del producto:", cantidad)
        print("Valor total: $", valortotal)
        print("Valor del descuento: $", descuento)
        print("Valor total con descuento: $", valordescuento)
    else:
        print("Error: Cantidad y valor deben ser mayores a cero.")
except ValueError:
    print("Error: Ingrese datos válidos .")