

# def generaPares(limite):
#     num=1  
#     miLista=[]

#     while num < limite:

#         miLista.append(num*2)

#         num = num + 1
#     return miLista

# print(generaPares(10))

#------------------------------------------------------

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento
ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Malaga","Alicante")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

