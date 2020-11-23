import mysql.connector

#conexion

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

 

# la conexion ha sido correcta?

#print(database)

cursor = database.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

print("########### muestra las bases de datos ###########\n")

for x in cursor:
    print(x)

#crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
print("########### muestra las tablas ###########\n")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel', 'Astra', 18500);")

coches = [
    ('seat','ibiza',5000),
    ('Renault','Clio',15000),
    ('Citroen','saxo',2000),
    ('mercedes','Clase c',35000)
] 

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s);", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio<=5000 AND marca='seat'")
result = cursor.fetchall()

print("##### todos mis autos ######\n")
for x in result:
    print(x[1],x[3])

print("##### el primer auto ######\n")
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()

print(coche)

#borrar 
cursor.execute("DELETE FROM vehiculos WHERE marca='mercedes'")
database.commit()


print(cursor.rowcount,"borrados!!")

#actualizar
cursor.execute("UPDATE vehiculos SET modelo='leon' WHERE marca='seat'")
database.commit()
print(cursor.rowcount,"actualizados!!")