# HERENCIA: es la posibilidad de compartir atributos y metodos 
#entre clases. y que diferentes clases hereden de otras

class persona:
    """
    nombre = ""
    apellidos = ""
    altura = ""
    edad = ""
    """

    def getnombre(self):
        return self.nombre

    def getapellido(self):
        return self.apellidos

    def getaltura(self):
        return self.altura

    def getedad(self):
        return self.edad

    def setnombre(self,nombre):
        self.nombre = nombre

    def setapellido(self,apellidos):
        self.apellidos = apellidos 
    
    def setaltura(self,altura):
        self.altura = altura

    def setedad(self,edad):
        self.edad = edad

    def caminar(self):
        return "estoy caminando"

    def hablar(self):
        return "estoy hablando"

    def dormir(self):
        return "estoy durmiendo"

class informatico(persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "html, css, javascript, php"
        self.experiencia = 5

    def getlenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "estoy programando"

    def reparar(self):
        return "estoy reparando el pc"

class tecredes(informatico):

    def __init__(self):
        super().__init__()
        self.auditarredes = 'experto'
        self.experiencaredes = 15

    def auditorias(self):
        return "estoy auditando una red"


