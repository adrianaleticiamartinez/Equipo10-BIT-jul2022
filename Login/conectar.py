import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="bbva")
conecta=conexion1.cursor()
conecta.execute("show tables")
for base in conecta:
    print(base)

conexion1.close()    



