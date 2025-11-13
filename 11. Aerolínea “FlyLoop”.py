# 11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
# Como viajero frecuente, quiero una función calcular_millas(viajes) 
# que reciba el número de viajes realizados y sume millas según la distancia:

# Viaje corto (< 1000 km): 500 millas
# Medio (1000–3000 km): 1000 millas
# Largo (> 3000 km): 2000 millas
# Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado.


def calcular_millas():
    millas = 0
    viajes = 0
    total = 0
    while True:
        millas = input("ingresa el numero de millas: ")    
          
        if millas == "fin":
            print("el numero de millas es: ", total)
            break    
        millas = int(millas)
        
        if millas < 1000:
            print("Viaje corto (< 1000 km): 500 millas")
            viajes += 1
            total += millas
            
        elif millas >= 1000 and millas < 3000:
            print("edio (1000–3000 km): 1000 millas")
            viajes += 1
            total += millas
            
        else:
            print("Largo (> 3000 km): 2000 millas")
            viajes += 1
            total += millas
calcular_millas() 