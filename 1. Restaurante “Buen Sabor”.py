# 1. Restaurante “Buen Sabor” – Cálculo de propina
# Como mesero, quiero una función calcular_propina(total_cuenta)
# que reciba el valor total de la cuenta y calcule la propina del 10%.
# Si el total es mayor de $100.000, aplicar el 15%.
# El programa debe mostrar el total final a pagar.


def calcularPropina(cuenta):
    if cuenta <= 100.000:
        propina = cuenta * 0.90
        total = propina + cuenta
        print("el total de la cuenta es de: ", total)
    else:
        propina = cuenta * 0.85
        total = propina + cuenta
        print("el total de la cuenta es de: ", total)
        
calcularPropina(100000)
