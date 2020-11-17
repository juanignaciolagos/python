import clases

persona = clases.persona()

persona.setnombre("Juan")
persona.setapellido("lagos")
persona.setaltura("171cm")
persona.setedad("1000 años")

print(f"la persona es: {persona.getnombre()} {persona.getapellido()} su altura es {persona.getaltura()} y su edad son {persona.getedad()}")
print(persona.hablar())

informatico = clases.informatico()

informatico.setnombre("Daniela")
informatico.setapellido("Sanchez")

print(persona.hablar())
print(f"el informatico es: {informatico.getnombre()} {informatico.getapellido()}")
print(informatico.getlenguajes())
print(informatico.reparar())
print(informatico.caminar())
print(informatico.experiencia)

print("-------------------------------------")

tecnico = clases.tecredes()

tecnico.setnombre("mr. robot")
tecnico.aprender("redes")


print(tecnico.auditarredes, tecnico.getlenguajes(),tecnico.getnombre(),tecnico.experiencia,tecnico.experiencaredes)


