"""
Modulos: son funcionalidades o programas ya hechos para ser reutilizados
https://docs.python.org/3/py-modindex.html
podemos conseguir modulos qu ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros modulos
"""

"""
#importar modulo propio
import mimodulo

mimodulo.holamundo("Juan Lagos")
print(mimodulo.holamundo("Juan Lagos"))

mimodulo.calculadora(5,5,True)
print(mimodulo.calculadora(5,5,True))
print(mimodulo.calculadora(5,5,False))

#importar solo una funcion
from mimodulo import holamundo

holamundo("Juan Lagos")

#importar todas las funciones 
from mimodulo import *

print(calculadora(10,5,False))

#modulo datetime

import datetime

print(datetime.date.today())

Fecha_completa = datetime.datetime.now()

print(Fecha_completa)
print(Fecha_completa.year)
print(Fecha_completa.month)
print(Fecha_completa.day)

fecha_personalizada = Fecha_completa.strftime("%d-%m-%yy, %H:%M:%S")

print("Mi fecha personalisada: ",fecha_personalizada)

print(datetime.datetime.now().timestamp())
"""

#modulo matematicas

import math 

print("Raiz cuadrada de 10: ",math.sqrt(10))
print("Numero pi: ",math.pi)
print("redondear a la alza: ",math.ceil(4.5635636456))
print("redondear a la baja: ",math.floor(4.5635636456))

#modulo random

import random

print("numero aleatorio entre 15 y 67: ",random.randint(15,67))