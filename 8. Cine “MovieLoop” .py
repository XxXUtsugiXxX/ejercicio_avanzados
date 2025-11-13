# 8. Cine “MovieLoop” – Calculadora de entradas
# Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
# Aplicar precio:

# Menores de 12 → $5.000
# De 12 a 59 → $8.000
# Mayores de 60 → $4.000
# Usar un while y condiciones.

def Calcular_entradas():
    edad = 1
    while edad != 0:
        edad = int(input("ingresa tu edad: "))
        if edad >= 1 and edad < 12:
            print("la boleta te vale 5.000")
        elif edad >= 12 and edad <= 59:
            print("la boleta vale 8.000")
        elif edad >= 60:
            print("la boleta vale 4.000")
    return edad
Calcular_entradas()