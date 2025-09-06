#------Ejercicio1-------
#for i in range (0,101):
#    print(i)

#------Ejercicio2-------
#numero = int(input("Ingresa un numero: "))
#digitos = 0
#if numero == 0:
#    digitos = 1
#else:
#    for i in range (0,10):
#        if numero == 0:
#            break
#        numero = numero // 10
#        digitos +=1 
#print(f"El numero tiene {digitos} digito/s")

#------Ejercicio3-------
#num1 = int(input("Ingresa un numero: "))
#num2 = int(input("Ingresa un numero: "))
#suma = 0
#if num1 > num2:
#    for i in range ((num2 + 1),(num1)):
#        suma += i   
#else: 
#    for i in range ((num1 + 1),(num2)):
#        suma += i   
#print(suma)

#------Ejercicio4-------
#salida = True
#suma = 0
#while salida != False:
#    numero = int(input("Ingresa un numero a sumar: "))
#    suma += numero
#    print(f"La suma es de: {suma}\n Ingrese 0 para salir")
#    if numero == 0:
#        print("Programa finalizado")
#        salida = False

#------Ejercicio5-------
#import random
#intentos = 0
#salida= True
#while salida != False:
#    numero = int(input("Adivina el numero aleatorio entre 0 y 9: "))
#    aleatorio = random.randrange(0,9)
#    intentos += 1
#    if numero == aleatorio:
#        salida = False
#print(f"Los intentos para encontrar: {aleatorio} fueron {intentos}")

#------Ejercicio6-------
#for i in range(100,0,-2):
#   print(i)

#------Ejercicio7-------
#num = int(input("Ingresa un numero: "))
#suma = 0
#for i in range(0,num + 1):
#    suma += i
#print(suma)

#------Ejercicio8-------
#par = 0
#impar = 0
#positivos = 0
#negativos = 0
#for i in range(0,10):
#    num = int(input("Ingresa un numero "))
#    if num > 0:
#        positivos += 1
#    if num % 2 == 0:
#        par += 1
#    if num % 2 == 1:
#        impar += 1
#    if num < 0:
#        negativos += 1
    #print(f"Positivos {positivos}\nNegativos {negativos}\nPares {par}\nImpares {impar}")


#------Ejercicio9-------
#suma = 0
#for i in range(0,10):
#    num = int(input("Ingresa un numero: "))
#    suma += num
#media = suma / 10
#print(f"La media entre los numeros ingresados es de: {media}")

#------Ejercicio10-------
#invertido = 0
#num = int(input("Ingresa un numero: "))
#numero = abs(num)
#while numero > 0:
#    digito = numero % 10         
#    invertido = invertido * 10 + digito  
#    numero = numero // 10 
#print(f"numero invertido: {invertido}")