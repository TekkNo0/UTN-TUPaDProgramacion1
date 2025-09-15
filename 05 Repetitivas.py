##EJERCICIO 1
#print("----------------*Encriptado*----------------")
#corrimiento = int(input("Ingrese el corrimiento deseado: "))
#abecedario = ["a","b","c","d","e","f","g","h",
#              "i","j","k","l","m","n","ñ","o",
#              "p","q","r","s","t","u","v","w",
#              "x","y","z"]

#letra = ""
#encriptado = ""


#for i in range(1, 6):
#    mensaje = input(f"Ingrese el mensaje {i} a mandar: ").lower()
#    encriptado = ""
#
#    for letra in mensaje:
#        if letra in abecedario:
#            posicion = abecedario.index(letra)
#            nueva_letra = abecedario[(posicion + corrimiento) % 27]
#            encriptado += nueva_letra
#        else:
#            encriptado += letra
#
#    print(f"Mensaje {i} encriptado: {encriptado}\n")   



##EJERCICIO 2
#import random
#opciones = ["piedra","papel","tijera"]
#menu = True

#while menu != False or eleccion != 5:
#    print("\t---------*Juego Clasico*--------- \n")
#    print("Ingrese su opción. \n \n (1)-> PIEDRA \t (2)-> PAPEL \t (3)-> TIJERA \n \n (4)-> SALIR \n")
#    eleccion = int(input("->"))
#    maquina = random.choice(opciones)
#    
#    if eleccion == 1:
#        print(f"La maquina eligió {maquina} \n")
#        if maquina == "piedra":
#            print("Empate")
#        elif maquina == "papel":
#            print("Perdiste")
#        else:
#            print("Ganaste")
#    if eleccion == 2:
#        print(f"La maquina eligió {maquina} \n")
#        if maquina == "piedra":
#            print("Ganaste")
#        elif maquina == "papel":
#            print("Empate")
#        else:
#            print("Perdiste")
#    if eleccion == 3:
#        print(f"La maquina eligió {maquina} \n")
#        if maquina == "piedra":
#            print("Perdiste")
#        elif maquina == "papel":
#            print("Ganaste")
#        else:
#            print("Empate")
#    if eleccion == 4:
#        break
#print("\t\t Juego terminado :)")        