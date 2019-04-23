
class Coche():

    def __init__(self):
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4    #Encapsulada con dos guiones bajos
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
            
        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha  ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un anche de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
        
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="mal"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False   

micoche=Coche()

print(micoche.arrancar(True))

micoche.estado()

print("----------------------A continuacion creamos el segundo objeto")

micoche2=Coche()

print(micoche2.arrancar(False))

micoche2.estado()




