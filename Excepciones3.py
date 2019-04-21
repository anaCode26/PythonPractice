
# edadPersona=int(input("Introduce tu edad:"))

# def evaluaEdad(edad):
 
#     if edad < 20:
#         return "eres muy joven"
#     elif edad < 40:
#         return "eres joven"
#     elif edad <65:
#         return "eres maduro"
#     elif edad<100:
#         return "cuidate..."
# print(evaluaEdad(edadPersona))

#-----------------------------------------------------

#   CALCULO DE RAIZ

import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("Numero no puede ser negativo")
    else:
        return math.sqrt(num1)

opc1 = int(input("Introduce un numero:"))

try:
    print(calculaRaiz(opc1))

except ValueError as ErrorDeNumeroNegativo:
    
    print(ErrorDeNumeroNegativo)

print("Programa terminado")