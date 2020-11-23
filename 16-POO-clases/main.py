# programacion orientada a objetos (POO o OOP)

#definir una clase (molde para crear mas objetos de ese tipo (coche) con caracteristicas similares)

print("---- COCHE 1 -----")

class coche:
    #atributos o propiedades (variables)
    #carac del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos son acciones que hace el objeto (coche) (funciones)
    def setcolor(self,color):
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def setmodelo(self,modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getvelocidad(self):
        return self.velocidad
    
# fin definicion clase / instanciar la clase

coche = coche()

coche.setcolor("amarillo")
coche.setmodelo("murcielago")

print(coche.marca,coche.getcolor(),coche.getmodelo())
print("velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("velocidad actual: ", coche.velocidad)

#crear mas objetos 

print("------COCHE 2 -------")

coche2 = coche

coche2.setcolor("verde")
coche2.setmodelo("Gallardo")


print(coche2.getmodelo(),coche2.getcolor(),coche2.getvelocidad())

print(type(coche2))

