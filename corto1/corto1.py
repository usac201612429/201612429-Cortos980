def inicio():
    n = 429                                     #mi numero de carné
    sucesiones = []                             #lista donde guardare n sucesiones
    for i in range(2, n + 1):                   #for para evaluar cada numero de 2 a n
        sucesion = []                           #lista donde guardare la n-esima sucesion
        while(i != 1):                          #ciclo para evaluar numeros hasta que se llegue a 1
            sucesion.append(int(i))             #agrego el siguiene valro de la sucesion
            if (i % 2 == 0):                    #numero es par?
                i /= 2                          #le asigno su valor dividido 2
            else:                               #de lo contrario
                i = 3 * i + 1                   #le asigno el tiple de su valor mas 1
        sucesion.append(1)                      #como el ciclo no entra al ser i = 1, le agrego el 1, se que no es lo mas eficiente
                                                #pero si lo primero que funcionó
        sucesiones.append(sucesion)             #agrego la n-esima sucesion a una sola lista
    with open("collatz.txt", "w") as f:         #abro archivo collatz, sino existe lo crea
        for secuencia in sucesiones:            #para cada sucesion la agrego al archivo
            f.write(str(secuencia) + "\n")

         

if __name__ == "__main__":                      #no lo comprendo bien pero entiendo que python
    inicio()                                    #busca el archivo __main__ y es justo el __name__
                                                #de este archivo
