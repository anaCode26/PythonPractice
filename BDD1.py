
import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BATE',20,'DEPORTES')")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('RAQUETA',25,'DEPORTES')")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('CAMISA',50,'ROPA')")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('ZAPATOS',130,'CALZADOS')")

# variosProductos=[
#     ("PANTALON",10,"DEPORTES"),
#     ("JARRON",90,"CERAMICA"),
#     ("CAMION",20,"JUGUETERIA")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()
for producto in variosProductos:
    print("Nombre del articulo: ",producto[0],"Precio: ", producto[1], "Seccion: ",producto[2])

miConexion.commit()

miConexion.close()