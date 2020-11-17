nombre = "Juan Lagos"

#funciones Generales

print(nombre)
print(type(nombre))

#detectar el tipado

comprobar = isinstance(nombre,int)

if comprobar:
    print("Esta variable es un string")
else:
    print("no es un string")

if not isinstance(nombre,float):
    print("la variable no es un numero decimal")

#limpiar espacios
frase = "     mi contenido    "
print(frase)
print(frase.strip())

#eliminar variables
year = 2020
print(year)
del year
#print(year)

#comprobar variable vacia
texto = "    FF    "

#largo de variable
print(len(texto))

#comprobar variable vacia
if len(texto) <=0: 
    print("esta variable esta vacia")
else:
    print("variable activa y tiene ",len(texto)," espacios")

print(isinstance(nombre,float))

#encontrar caracteres 

frase = "la vida es bella"
print(frase.find("vida"))

# Mayusculas y minusculas 
print(nombre)
print(nombre.upper())
print(nombre.lower())
