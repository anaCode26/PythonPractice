
class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Lugar de residencia: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nom_empleado,edad_empleado,res_empleado):
        super().__init__(nom_empleado,edad_empleado,res_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
     
    def descripcion(self):
        super().descripcion()
        print("El salario es: ",self.salario, "Y los años de antiguedad son: ", self.antiguedad)
            
Maria=Empleado(2000,10,"Maria",27,"Valencia")

Maria.descripcion()

print(isinstance(Maria,Empleado))
