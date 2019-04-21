
class Coche():

    def __init__(self):
        
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4    #Encapsulada con dos guiones bajos
        self.enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un anche de ", self.anchoChasis, 
        " y un largo de ", self.largoChasis)
        
micoche=Coche()

print("El largo de mi coche es: " ,micoche.largoChasis)
print("El coche tiene ", micoche.__ruedas, " ruedas")

print(micoche.arrancar(True))

print(micoche.estado())

print("----------------------A continuacion creamos el segundo objeto")

micoche2=Coche()

print("El largo de mi coche es: " ,micoche2.largoChasis)
print("El coche tiene ", micoche2.__ruedas, " ruedas")

print(micoche2.arrancar(False))

print(micoche2.estado())




