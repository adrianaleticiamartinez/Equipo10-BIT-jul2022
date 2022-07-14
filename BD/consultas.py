import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", passwd="",database="bbva")
conecta=db.cursor()


query = "SELECT usuario FROM  baseusuarios"
conecta.execute(query)

usuarios = conecta.fetchall()
for x in usuarios:
    print (x)

db.close()


