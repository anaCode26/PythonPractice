print("Programa de evaluacion de notas")

nota_alumno = int(input("Introduzca nota del alumno:"))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(nota_alumno))