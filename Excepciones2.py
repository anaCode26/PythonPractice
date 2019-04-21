
def divide():
    try:
        opc1=float(input("Introduce el primer numero:"))
        opc2=float(input("Introduce el segundo numero:"))

        print("La division es: " + str(opc1/opc2))

    except ValueError:

        print("El valor introducido es erróneo")

    except ZeroDivisionError:

        print("No se puede dividir entre cero 0!")

    print("Calculo finalizado")

divide()
