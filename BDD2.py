
import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20))
    ''')
productos=[

    ("PELOTA",20,"JUGUETERIA"),
    ("PANTALON",15,"CONFECCION"),
    ("DESTONILLADOR",25,"FERRETERIA"),
    ("JARRON",45,"CERAMICA")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

miConexion.commit()

miConexion.close()

