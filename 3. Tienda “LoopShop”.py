# 3. Tienda “LoopShop” – Descuentos acumulados
# Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
# Si el precio supera 50.000, aplicar 10% de descuento.
# Al final, mostrar la suma total de las compras con descuento.

def aplicar_descuentos():
    total = 0

    while True:
        monto = int(input("Ingresa el monto a pagar (0 para terminar): "))
        if monto == 0:
            break  
        total += monto

    if total >= 50000:
        total *= 0.90
        print("Se aplicó un descuento del 10%")

    print("Este es el total a pagar:", total)


aplicar_descuentos()
