"""
mostrar todas las tablas de multiplicar del 1 al 10 
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

"""

for cabecera in range(1,11): 
    print(f"###tabla del {cabecera}###")
    for contador in range(1,11):
        print(f"{cabecera}X{contador}={contador*cabecera}")
    print("##################") 
 