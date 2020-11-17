#capturar excepciones y manejar errores en codigo susceprible a fallas o errores
"""
try:
    nombre = input("¿Cuale es tu nombre?")

    if len(nombre)>1:
        nombre_usuario = "el nombre es: " + nombre

    print(nombre_usuario)
except:
    print("ha ocurrido un error, mete bien el nombre")
else:
    print("todo a funcionado correctamente")
finally:
    print("fin de la iteracion")


#multiples exepciones: 
try:
    numero = int(input("numero para elevarlo al cuadrado: "))
    print("el cuadrado del numero es: " + str(numero*numero))
except TypeError:
    print("debes convertir tus cadenas a enteros")
except ValueError:
    print("introduce un numero no letras ni otro tipo de dato")
except Exception as e:
    print(type(e))
    print("ha ocurrido un error: ",type(e).__name__)
"""

#exepciones personalizadas o lanzar excepcion
try:
    nombre = input("introduce el nombre: ")
    edad = int(input("introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("la edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("el nombre no esta completo")
    else:
        print(f"bienvenido al master en python: {nombre}")
except ValueError:
    print("introduce los datos correctamente")