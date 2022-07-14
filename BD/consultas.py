from ast import If
import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", passwd="",database="bbva")
conecta=db.cursor()

#Consulta para manager
dato = input("idCliente para manager: ")
query = "SELECT * FROM libropeque WHERE idCliente = '{}'".format(dato)
conecta.execute(query)
usuarios = conecta.fetchall()
for x in usuarios:
    print (x)


#Consulta para restringuida
dato1 = input("idCliente restringuido: ")
query = "SELECT nombre,apellidoPaterno,sexo,rfc FROM libropeque WHERE idCliente = '{}'".format(dato1)
conecta.execute(query)
usuarios = conecta.fetchall()
for x in usuarios:
    print (x)

#Consulta para validador
dato3 = input("idCliente: ")

query = "SELECT nombre FROM libropeque WHERE idCliente = '{}'".format(dato3)
conecta.execute(query)
usuarios = conecta.fetchall()
for x in usuarios:
    print (x)

db.close()

