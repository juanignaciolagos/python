"""
# FOR 

For variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0 
resultado = 0

for contador in range(0, 10):
    print("voy por el: "+ str(contador))

    resultado = resultado  + contador
    
print(F"el resultado es :  {resultado}")

print("\n#########EJEMPLO########")

numero_usuario = int(input("De que numero quieres la tabla: "))

if numero_usuario < 1:

    numero_usuario = 1

print(F"\ntabla de multiplicar del numero del usuario: {numero_usuario}")

for numero_tabla in range(1,11):

    if numero_usuario == 45:
        print("numero prohibido")
        break

    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
    

else:
   print(f"tabla del numero {numero_usuario} finalizada")

