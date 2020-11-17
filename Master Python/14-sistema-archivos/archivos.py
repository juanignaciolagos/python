from io import open
import pathlib
import shutil
import os
import os.path

"""
#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#print(ruta)
archivo = open(ruta,"a+")

#escribir

archivo.write("****** Soy Un texto escrito desde python*****\n")

#cerrar archivo

archivo.close()


#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r")

#leer un archivo
#contenido = archivo_lectura.read()

#print(contenido)

#leer contenido y guardarlo en lista

lista =  archivo_lectura.readlines()
archivo_lectura.close()
print(lista)



for x in lista:
    #lista_x = x.split()
    #print(lista_x)
    if not x.isnumeric(): 
        print("- " + x.upper())


#copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "../07-Ejercicios/fichero_copiado.txt"
shutil.copyfile(ruta_original,ruta_nueva)
"""

#mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

#shutil.move(ruta_original,ruta_nueva)

#eliminar
"""
os.remove(ruta_nueva)
"""
#comprobar si existe
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)
print(os.path.abspath("./"))

if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("el archivo no existe")
