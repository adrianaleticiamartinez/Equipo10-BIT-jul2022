import csv

#print("Ingrese el identificador del usuario")
#uid= input()
#print("Ingrese el password")
#password = input()

uid = 'EduardoE'
with open('baseUsuarios.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        datos=row
        if(datos[0] == uid):
            usuario = datos[0]
            perfil = datos[6]
            print(datos)

print("Ingrese el iID del Cliente")
idCliente = input()

def buscarUsuarios(idCliente,perfil):
    if(perfil == "Manager"):
        print('entrando a Manager')
        with open('baseClientesHackaton2022.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                datos = row
                if(datos[0] == idCliente):
                    print(datos)
                    break

    elif(perfil == "Validador"):
        print()

    elif(perfil == "Restringido"):
        print()

buscarUsuarios(idCliente,perfil)
