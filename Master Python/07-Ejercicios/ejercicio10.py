"""

El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla quienes han aprobado y quienes han suspendido 

"""

contador = 1
aprobados = 0 
suspendidos = 0

numero_de_alumnos = int(input("cuantos alumnos tienes: "))

while contador <= numero_de_alumnos:
    nota = int(input(f"que nota quieres ponerle a \"alumno {contador}\"?: "))

    if nota >= 3:
        aprobados += 1
    else:
        suspendidos += 1
    
    contador += 1

print(f"Total Aprobados: {aprobados}")
print(f"Total Reporbados; {suspendidos}")