# 13. Tienda Online “ShopMaster” – Carrito de compras con validaciones
# Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

# Si el precio es negativo, mostrar error y pedir otro valor.
# Si el precio es mayor a 100.000, aplicar un 20% de descuento.
# Usar while y if dentro de la función hasta ingresar 0 para finalizar.

def carrito():
    preciot = 0
    precio = 1
    total = 0
    while precio != 0:
        
        precio = int(input("digite el precio del producto: "))
         
        if precio < 0:
            precio = int(input("Error digita un numero > 0: "))
            continue
     
        if precio > 100000:
            total = preciot + precio
            total *= 0.80
            
            print("el total es: ", total)
        else:
            preciot += precio
            print("el total eslkn: ", preciot)
            
carrito()