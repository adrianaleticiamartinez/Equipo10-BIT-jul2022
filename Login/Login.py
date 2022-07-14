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


def buscarUsuarios(idCliente,rol):
    if(rol == "Manager"):
        print()
    elif(rol == "Validador"):
        print()
    else:(rol == "Restringido")
        print()



