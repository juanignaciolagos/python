import os
import shutil

"""
#crear carpeta

if not os.path.isdir ("./micarpeta"):
    os.mkdir("./micarpeta")
else:
    print("ya existe el directorio")

#eliminar
#os.rmdir('./micarpeta')
"""

#copiar

ruta_original = "./micarpeta"
ruta_nueva = "./micarpeta_copiada"

#shutil.copytree(ruta_original,ruta_nueva)

#eliminar
#os.rmdir('./micarpeta_copiada')

print("contenido de mi carpeta")

contenido = os.listdir("./micarpeta")

print(contenido)

for x in contenido:
    print(f"Archivo: {x}")
