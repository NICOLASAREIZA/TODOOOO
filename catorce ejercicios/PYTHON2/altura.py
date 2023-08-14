def calcular_altura():
    altura = input('Altura: ')
    iniciales = input('Iniciales: ')

    if iniciales.isdigit() or "-" in altura:
        print("Error, ingresa datos válidos")
        return

    if iniciales and altura:
        porciones = altura.split(' ')

        if altura.replace('.', '', 1).isdigit():
            altura_numero = float(altura)
            metros = int(altura_numero)
            centimetros = round((altura_numero - metros) * 100)
            resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + (str(metros) + " centímetro" + ("s" if metros != 1 else "")) + (" con " + str(centimetros) + " centímetro" + ("s" if centimetros != 1 else "") if centimetros > 0 else "")
            print(resultado)
        elif len(porciones) == 2 and porciones[1] == "cm" and porciones[0].isdigit():
            centimetros = int(porciones[0])
            resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + str(centimetros) + " cm"
            print(resultado)
        elif len(porciones) == 2 and porciones[0].isdigit() and porciones[1].replace('.', '', 1).isdigit():
            metros = int(porciones[0])
            centimetros = int(float(porciones[1]) * 100)
            resultado = "Tus iniciales son: " + iniciales + " y tu altura es de " + (str(metros) + " metro" + ("s" if metros != 1 else "")) + (" con " + str(centimetros) + " centímetro" + ("s" if centimetros != 1 else "") if centimetros > 0 else "")
            print(resultado)
        else:
            print("Error, ingresa datos válidos")
    else:
        print("Error, ingresa datos válidos")

calcular_altura()
