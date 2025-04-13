with open("informacion.txt","r",encoding="utf-8") as contenido:
    filas = contenido.readlines() #Leo cada linea del archivo informacion

for i, fila in enumerate(filas,start=1): #Recorro cada linea haciendo uso de enumerate empezando a numerar desde 1
    fila = fila.strip() # borro los espacios de ser que existan
    datos = fila.split(";") # guardo en lista cada dato delimitado por ;

    if len(datos) !=4: #si una linea de datos es diferente de 4
        print("No hay elemento")
        continue #de llegar a haber este error continua con lo demas

#guardamos informacion en cada variable
    name = datos[0]
    lastname = datos[1]
    direc = datos[2]
    correo = datos[3]
#imprimo informacion para poderla visualizar
    print("Nombre: ", name)
    print("Apellido: ", lastname)
    print("Lugar: ", direc)
    print("Correo: ", correo)
    print("----------------------------------------------")
