# edad=20

# if 0<edad<100:
#     print("Edad correcta")
# else:
#     print("Edad inconrrecta")

#---------------------------------------------------------------------
salario_presidente = int(input("Introduce salario del presidente:"))
print("Salario presidente:" + str(salario_presidente))

salario_director = int(input("Introduce salario del director:"))
print("Salario director:" + str(salario_director))

salario_jefe_area = int(input("Introduce salario del jefe de area:"))
print("Salario jefe de area:" + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario del administrativo:"))
print("Salario administrativo:" + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")




