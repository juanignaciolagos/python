from coche import coche

carro = coche("amarillo","renault","clio",150,200,4)
carro1 = coche("verde","seat","panda",240,200,4)
carro2 = coche("azul","citroen","zara",100,180,4)
carro3 = coche("rojo","mercedes","clase a",250,400,4)

print(carro.getinfo())
print(carro1.getinfo())
print(carro2.getinfo())
print(carro3.getinfo())

#detectar tipado
#carro3 = "sdfsd"

if type(carro3) == coche:
    print("es un objeto correcto")
else:
    print("no es un objeto")

# Visibilidad

print(carro.getprivado())