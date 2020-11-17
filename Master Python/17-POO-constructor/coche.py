class coche:
    #atributos o propiedades (variables)
    #carac del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "hola soy un atrubuto publico"
    __soy_privado = "hola soy un atributo privado"

    def getprivado(self):
        return self.__soy_privado


    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    # metodos son acciones que hace el objeto (coche) (funciones)
    def setcolor(self,color):
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def setmarca(self,marca):
        self.marca = marca
    
    def getmarca(self):
        return self.marca

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

    def getinfo(self):

        info = "--------informacion del coche---------"
        info += "\n color: " + self.getcolor()
        info += "\n marca: " + self.getmarca()
        info += "\n modelo: " + self.getmodelo()
        info += "\n velocidad: " + str(self.getvelocidad())
        
        return info
