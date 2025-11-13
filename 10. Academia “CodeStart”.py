# 10. Academia “CodeStart” – Tabla de multiplicar personalizada
# Como estudiante, quiero una función tabla_multiplicar(numero)
# que use un for para mostrar la tabla del número dado hasta el 10.
# Si el resultado es mayor de 50, mostrar también “Resultado alto”.


def tabla_multiplicar(numero):
    numero = int(input("digita el numero que quieres conocer la tabla hasta el 10: "))
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        resultado = numero * i
        if resultado > 50:
            print("es muy alto")
            
tabla_multiplicar(10)