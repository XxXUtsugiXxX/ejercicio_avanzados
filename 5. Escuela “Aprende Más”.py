# 5. Escuela “Aprende Más” – Promedio de notas
# Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
# Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
# Debe repetirse para varios estudiantes usando un while.


def promedio_notas():
    estudiantes = 0
    total = 0
    while estudiantes != 4:
        nota1 = float(input("ingresa la primera nota: "))
        nota2 = float(input("ingresa la segunda nota: "))
        nota3 = float(input("ingresa la tercera nota: "))
        total = (nota1 + nota2 + nota3) / 3
        estudiantes += 1
        if total >= 3:
            print("aprobaste")
        else:
            print("Reprobado")
            
promedio_notas()
        