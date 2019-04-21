print("Programa de becas año 2019")

distancia_escuela=int(input("Introduce la distancia a la escuela en km:"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro:"))
print(numero_hermanos)

salario_anual=int(input("Introduce salario familiar:"))
print(salario_anual)

if distancia_escuela >  40 and numero_hermanos > 2 or salario_anual <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a becas")


#----------------------------------------------------------------------

print("Asignatura optativa año 2019")
print("Asignatura optativas: Informatica - Pruebas de software - Usabilidad y accesibilidad")

opcion= input("Escribe una asignatura:")
asignatura=opcion.lower()

if asignatura in ("informatica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")



