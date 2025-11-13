# 6. Estación “LoopBus” – Simulador de pasajeros
# Como conductor, quiero una función simular_viaje(pasajeros)
# que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
# Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle.

def simular_viaje():
    for i in range(0, 11):
        i+=1
        if i <= 10:
            print(f"Pasajero {i} a bordo")
        else:
            print("bus lleno")
            break
       
    return i
simular_viaje() 