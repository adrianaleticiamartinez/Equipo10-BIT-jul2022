import mysql.connector
import csv

count=0
with open(r"C:\Users\Angel\Desktop\BBVA BIT\Python\Equipo10-BIT-jul2022\BD\baseClientesHackaton2022.csv", newline='') as File:  
    reader = csv.reader(File, delimiter=',')
    for row in reader:
        print(row)
        count = count + 1
        if(count == 10):
            exit()


conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="bbva")
conecta=conexion1.cursor()
conecta.execute("show tables")
for base in conecta:
    print(base)

conecta.close()
conexion1.close()  