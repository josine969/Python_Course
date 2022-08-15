# Create a program to calculate salary from employee based on his extra hours

from ast import Try
valor = -1
valor2 = -1

while valor < 0:
    print("¿Cuantas horas has trabajado?")
    Horas = input()

    try:
        valor = int(Horas)
    except:
        valor = -1

    if valor > 0:
        print("Has trabajado", valor)
    else:
        print("No has introducido un numero")

while valor2 < 0:
    print("¿Que nivel profesional tienes?")
    Nivel = input()

    try:
        valor2 = int(Nivel)
    except:
        valor2 = -1
    if valor2 > 0:
        print("Tu nivel profesional es", valor2)
    else:
        print("No has introducido un numero")
    
print ("Te corresponde", valor*valor2, "por haber trabajado", valor, "horas y tener el nivel profesional", valor2)