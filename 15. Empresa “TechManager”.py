# 15. Empresa “TechManager” – Simulador de rendimiento laboral
# Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

# Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
# Si la hora es mayor de 8, contar como hora extra.
# Al final, calcular el total de horas normales y extras.
# Mostrar un resumen del empleado.

def evaluar_empleado(nombre, horas):
    contador = 0
    for i in range (1, horas+1):
        
        if i > 8:
            contador += 1
            print(f"el trabajador {nombre} ha trabajado {i} y {contador} horas extras ")
        else:
            print(f"el trabajador {nombre} ha trabajado: {i}")
            
evaluar_empleado("brayhan",10)