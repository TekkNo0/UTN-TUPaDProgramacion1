#-----------EJERCICIO1-------------
#edad = int(input("Ingrese su edad: "))
#if edad >= 18:
#    print("Es mayor de 18 años")

#-----------EJERCICIO2-------------
#nota = int(input("Ingrese su nota: "))
#if nota >= 6:
#    print("Estas aprobado")
#else:
#    print("Estas desaprobado")

#-----------EJERCICIO3-------------
#num = int(input("Ingresa un número par: "))
#if num % 2 == 0:
#    print("Es un número par")
#else:
#    print("Número impar")


#-----------EJERCICIO4-------------
#edad = int(input("Ingresa tu edad: "))
#if edad < 12:
#    print("Niño")
#elif edad >= 12 and edad < 18:
#    print("Adolescente")
#elif edad >= 18 and edad < 30:
#    print("Adulto joven")
#else:
#    print("Adulto")


#-----------EJERCICIO5-------------
#contraseña = str(input("Ingresa una contraseña: "))
#longitud = len(contraseña)
#if longitud >= 8 and longitud <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#   print("Contraseña Incorrecta")

#-----------EJERCICIO6-------------
#from statistics import mode, median, mean
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#moda = mode(numeros_aleatorios)
#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#if media > mediana and mediana > moda:
#    print("Sesgo Positivo")
#elif media < mediana and mediana < moda:
#    print("Sesgo Negativo")
#elif media == mediana and media == moda:
#    print("Sin sesgo")


#-----------EJERCICIO7-------------
#frase =str(input("Ingrese una frase: "))
#longitud = len(frase)
#vocales = ["a","e","i","o","u"]
#letra = frase[longitud-1]
#if letra in vocales:
#    print(f"{frase}!")
#else:
#    print(frase)


#-----------EJERCICIO8-------------
#nombre = str(input("Ingresa tu nombre: "))
#print("OPCIONES \n (1)->Mayusculas \t (2)->Minusculas \t (3)->Primer letra mayus")
#opcion = int(input("Ingresa que opción quieres usar: "))
#if opcion == 1:
#    nombre = nombre.upper()
#    print(nombre)
#elif opcion == 2:
#    nombre = nombre.lower()
#    print(nombre)
#elif opcion == 3:
#    nombre = nombre.title()
#    print(nombre)   

#-----------EJERCICIO9-------------
#magnitud = int(input("Ingresa la magnitud del terremoto: "))
#if magnitud <= 3:
#    print("Muy leve")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve")
#lif magnitud >= 4 and magnitud < 5:
#    print("Moderado")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy fuerte")
#else:
#    print("Extremo")


#-----------EJERCICIO10-------------
hemisferio = str(input("Ingrese el hemisferio en el que se encuentra (sur o norte): ")).lower()

mes = str(input("Ingrese el mes actual: ")).lower()
dia = int(input("Ingrese el dia actual: "))

if dia > 0 and dia < 31:
    if hemisferio == "sur":
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
            print("Se encuentra en Verano")
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
            print("Se encuentra en Otoño")
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
            print("Se encuentra en Invierno")
        elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
            print("Se encuentra en Primavera")
        else:
            print("Fecha mal dada")
    

    if hemisferio == "norte":
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
            print("Se encuentra en Invierno")
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
            print("Se encuentra en Primavera")
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
            print("Se encuentra en Verano")
        elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
            print("Se encuentra en Otoño")
        else:
            print("Fecha mal dada")
else:
        print("Fecha mal dada")