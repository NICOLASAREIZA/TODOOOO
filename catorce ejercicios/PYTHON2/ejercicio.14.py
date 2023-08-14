# Se tienen un cultivo de café, de los cuales con el uso de la tecnología se recolectan los
# siguientes datos para análisis de suelo:
# PH (Acidez del suelo) rango adecuado entre 5 y 5.5.
# Materia orgánica mayor a 8
# Fosforo (P) mayor a 30
# Calcio (Ca) mayor a 3
# Magnesio (Mg) mayor a 0.9
# Potasio (K) mayor a 0.4
# Aluminio (Al) menor a 1
# Acorde a los datos recolectados identificar si el suelo es apto para la siembra café


ph = float(input("Acides del suelo: "))
materialorganica = float(input("Materia Organica: "))
fosforo = float(input("Fosforo: "));
calcio = float(input("Calcio: "));
magnesio = float(input("Magnesio: "));
potasio = float(input("Potasio: "));
aluminio = float(input("Aluminio: "));


if ph >= 5 and ph <= 5.5 and materialorganica > 8 and fosforo > 30 and calcio > 3 and magnesio > 0.9 and potasio > 0.4 and aluminio < 1:
    print("El suelo es apto")
else:
    print("El suelo no es apto")