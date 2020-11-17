
import usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("\nOK!! vamos a registrarte en el sistema...")
        nombre = input("\nintroduce tu nombre: ")
        apellidos = input("\nintroduce tu apellido: ")
        email = input("\nintroduce tu email: ")
        password = input("\nintroduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registar()

        if registro[0] >=1:
            print(f"\nperfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nno te has registrado correctamente!!!!")

    def login(self):
        print("\nOK!! vamos a identificarte en el sistema")
        email = input("\nintroduce tu email: ")
        password = input("\nintroduce tu contraseña: ")

        usuario = modelo.Usuario('','', email, password)
        login = usuario.identificar()

        if email == login[3]:
            print(F"Bienvenido {login[1]} te has registrado en el sistema el {login[5]}")