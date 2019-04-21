
# i=1

# while i<=10:
#     print("Ejecucion " + str(i))
#     i=i+1

# print("Terminó la ejecución")

#----------------------------------------------------

# edad=int(input("Introduce tu edad:"))

# while edad < 0:
#     print("Has introducido una edad negativa. Vuelve a intentarlo")
#     edad=int(input("Introduce tu edad:"))
# print("Gracias por colaborar")
# print("Edad del aspirante " + str(edad))

#----------------------------------------------------------
import math

print("Pograma de calculo de raiz cuadrada")
numero=int(input("Introduce un numero:"))
intentos=0

while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido muhcos intentos. El programa ha finalizado")
        break;
    numero = int(input("Introduce un numero:"))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " +str(numero) + " es " + str(solucion))


