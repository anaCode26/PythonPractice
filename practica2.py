#Haciendo una funcion

# def saludos():
#     print("holis")
# saludos()
# saludos()
# saludos()

#-----------------------------------------------

# def suma(a,b):
#     return a+b
# print(suma(3,4))

#-----------------------------------------------

# def Multiplicar():   
#     x=int(input("Ingrese un numero:"))
#     y=int(input("Ingrese un numero:"))
#     return x*y
# print(Multiplicar())

#-----------------------------------------------

class Heredada:
    def chao(self):
        print("chao")
    

class Miclase(Heredada):
    def hola(self):
        print("hola")
a = Miclase()
a.hola()

a.chao()









