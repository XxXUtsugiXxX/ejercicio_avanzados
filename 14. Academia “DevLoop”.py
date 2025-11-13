# 14. Academia “DevLoop” – Calculadora de factoriales
# Como estudiante de programación, quiero una función calcular_factorial(numero)
# que use un bucle for para calcular el factorial del número.
# Si el número ingresado es negativo, mostrar “Número inválido”.
# De lo contrario, mostrar el resultado.

def Clcular_factorial():
    numero = int(input("ingresa el numero que quieres saber el factorial: "))
    while numero <= 0:
        numero = int(input("numero invalido: "))
        
    for i in range (numero):
        i += 1
        numero *= i
        print(numero)
         
Clcular_factorial()