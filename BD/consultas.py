import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", passwd="",database="bbva")
conecta=db.cursor()

dato = input("Dato: ")

query = "SELECT idCliente,nombre,nacionalidad FROM libropeque WHERE nombre = 'Abril'"
conecta.execute(query)

usuarios = conecta.fetchall()
for x in usuarios:
    print (x)

db.close()





