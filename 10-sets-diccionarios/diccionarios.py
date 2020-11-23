"""
diccionario:
es un tipo de datos que almacena un conjunto de datos.
en formato clave > valor.
es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "juan",
    "apellidos": "lagos",
    "web":"juan.cl"
}
"""
print(type(persona))
print(persona)
print(persona["apellidos"])
"""

# lista con diccionarios

contactos = [
    {
        "nombre": "juan",
        "email": "juan@juan.com"    
    },
    {
        "nombre": "luis",
        "email": "luis@luis.com"
    },
    {
        "nombre": "salvador",
        "email": "salvador@salvador.com"
    }
]


contactos[0]["nombre"] = "juanito"
#print(contactos[0]["nombre"])

print("\nlistadocontactos: ")

for x in contactos:
    print(f"Nombre del contacto: {x['nombre']}")
    print(f"email del contacto: {x['email']}")
    print("------------------------------------------")
