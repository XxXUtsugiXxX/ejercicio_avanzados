# 7. Panadería “Don Pancho” – Control de producción diaria
# Como panadero, quiero una función hornear_pan(lotes) 
# que use un for para indicar qué lote se está horneando.
# Si el lote es divisible por 3, mostrar “Verificación de calidad”.
# Al final, mostrar “Producción terminada”.

def hornear_pan(lotes):
    for i in range(lotes):
        i += 1
        if i % 3 == 0:
            print("Verificacion de calidad")
        else:
            print("lote numero: ", i)

    print("Produccion terminada")
hornear_pan(5)
print("si soy marica")