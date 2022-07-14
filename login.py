from getpass import getpass

usuarioRegistrado = "alopez@m3sec.mx"
contraseña = "Secure99"
rol="Manager"

flag = 1
intentos = 3

while(flag == 1):
    print("Ingrese el identificador del usuario")
    uid= input()
    password= getpass()
    if(usuarioRegistrado != uid or contraseña != password):
        print("Login incorrecto")
        intentos = intentos - 1
        print("Te quedan "+str(intentos)+" intentosde login")
        flag = 1
    else:
        flag = 0
        print("Login correcto")
    if(intentos == 0):
        exit()


import csv

with open('baseUsuarios.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        datos=row
        rol = datos[6]
     #   print(perfil)
        if(perfil == "Manager"):
            print(datos)

def buscarUsuarios(idCliente,rol):
    if(rol == "Manager"):
        idCliente = input("Ingresa el ID a buscar: ")
        fila.execute("*SELECT *FROM Equipo10-BIT-jul2022/baseClientesHackaton.csv WHERE idCliente=?", (idCliente,) )
        datos = row.fetchall()
        print(datos)
    elif(rol == "Validador"):
        print()
    else:
        print()