

from io import open

## CREAR ARCHIVO DE TEXTO

#archivo_texto = open("archivo.txt", "w")

# frase="Estupendo dìa para estudiar python"

# archivo_texto.write(frase)

# archivo_texto.close()

## LEER ARCHIVO DE TEXTO

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)
