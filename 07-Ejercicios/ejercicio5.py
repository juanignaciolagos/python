"""

hacer un programa que muestres todos los numeros a partir de dos numeros que muestre el usuario

"""

numero1 = int(input("Introduce el numero 1: "))
numero2 = int(input("Introduce el numero 2: "))

if numero1 <= numero2:
   for contador in range(numero1,numero2 + 1):
        print(contador)
else:
  
   for contador in range(numero2,numero1 + 1):
        print(contador)