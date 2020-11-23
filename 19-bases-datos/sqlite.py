
import sqlite3 

#conexion a sqlite
#conexion = sqlite3.connect('pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio int(255)"
")")

#guardar cambios
conexion.commit()

"""
#insertar datos 
cursor.execute("INSERT INTO productos VALUES (null, 'primer producto','descripcion de mi segundo producto', 550)")
conexion.commit()
"""
#borrar datos 
#cursor.execute("DELETE FROM productos")
#conexion.commit()

#insertar multiples registros de golpe
"""
productos = [
    ("ordenador portatil","buen pc", 700),
    ("telefono movil","buen telfono", 150),
    ("placa base","buen placa", 80),
    ("tablet","buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()
"""
#cambiar datos 
cursor.execute("UPDATE productos SET precio=678 WHERE precio =80")


#leer datos de una tabla (listar datos)
cursor.execute("SELECT * FROM productos WHERE precio >=300;")
productos = cursor.fetchall()

for x in productos:
    print("ID: " + str(x[0]))
    print("titulo: " + x[1])
    print("descripcion: " + x[2])
    print("precio: " + str(x[3]))
    print("\n")

print("##################################")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#cerrar conexion 
conexion.close()

