"""
Crear un script que tenga 4 vsariables:
una lista, un string, un entero y un booleano
y que imprima un mensaje segun el tipo de dato de cada variable.
usar funciones
"""

lista = ["juan","dani",1,2,3]
texto = "variable texto"
entero = 2020
boooleano = True

def tipodedato(vari):
    if type(vari) == str:
        print(f"la variable {vari} es un texto")
    elif type(vari) == list:
        print(f"la variable {vari} es una lista")
    elif type(vari) == bool:  
        print(f"la variable {vari} es un dato boleano") 
    elif type(vari) == int:  
        print(f"la variable {vari} es un entero") 
    else:
        print(f"la variable {vari} esta no es entero, booleano, string, lista o puede estar vacia")


tipodedato(entero)

def comprobartipado(dato,tipo):
    test= isinstance(dato,tipo)
    result = ""

    if test:
        result = f"este dato es del tipo {type(dato)}"
    else:
        result = "el tipo de dato no es correcto"
    
    return result


print(comprobartipado(lista,list))
print(comprobartipado(lista,int))
print(comprobartipado(texto,str))


def traductor(vari):
    traducir = None
    
    if type(vari) == str:
        traducir = f"la variable {vari} es un texto"
    elif type(vari) == list:
        traducir = f"la variable {vari} es una lista"
    elif type(vari) == bool:  
        traducir = f"la variable {vari} es un dato boleano"
    elif type(vari) == int:  
        traducir = f"la variable {vari} es un entero"
    else:
        traducir = f"la variable {vari} esta no es entero, booleano, string, lista o puede estar vacia"

    return traducir

print(traductor(texto))