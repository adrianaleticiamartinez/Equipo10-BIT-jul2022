import csv

with open('baseUsuarios.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        datos=row
        perfil = datos[6]
     #   print(perfil)
        if(perfil == "Manager"):
            print(datos)
    
