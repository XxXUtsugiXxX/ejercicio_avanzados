# 12. Hospital “Salud Total” – Evaluador de signos vitales
# Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
# Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
# Repetir el proceso con varios pacientes en un bucle while.


def evaluar_paciente():
    pacientes = 0
    while pacientes != 4:
        FC = int(input("ingresa la frecuencia cardiaca: "))
        temp = int(input("ingresa la temperatura corporal: "))
        if FC > 100 and temp >38:
            print(f"Paciente en observacion frecuencia {FC} y la temperatura {temp}")
            pacientes += 1
        else:
            print("paciente con signos normales")
            pacientes += 1
evaluar_paciente()