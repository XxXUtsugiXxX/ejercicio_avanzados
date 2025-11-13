# 9. Tienda “EnergyStore” – Simulador de puntos
# Como cliente, quiero una función calcular_puntos(compras) 
# que use un for para recorrer la cantidad de compras (ingresada por el usuario).
# Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
# Al final, mostrar los puntos totales.


def Calcular_puntos():
    puntos = 0
    compras = int(input("digita el numero de compras: "))
    for i in range(1, compras+1):
        if i % 3 == 0:
            puntos += 10
            print(f"compra numero {i} se te agregaron 10 puntos ", puntos)
        else:
            puntos += 5
            print(f"compra numero {i} se te agregaron 5 puntos ", puntos)
        
Calcular_puntos()