#Ejercicio 1
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#precios_frutas["Naranja"] = 1200
#precios_frutas["Manzana"] = 1500
#precios_frutas["Pera"] = 2300


#Ejercicio 2
#precios_frutas["Banana"] = 1330
#precios_frutas["Manzana"] = 1700
#precios_frutas["Melón"] = 2800


#Ejercicio 3
#lista = list(precios_frutas.keys())

#Ejercicio 4
#dict_contactos = {}
#for i in range(1,3):
#    nombre = str(input(f"Ingresa el nombre del contacto {i}: "))
#    contacto = int(input(f"Ingresa el numero del contacto {i}: "))
#    dict_contactos[nombre] = contacto   
#print(dict_contactos)
#
#consulta = str(input("Ingresa el nombre a consultar: "))
#if consulta in dict_contactos:
#    print("Contacto:", dict_contactos.get(consulta))
#else:
#    print("Nombre no encontrado")

#Ejercicio 5
#palabra = str(input("Ingrese una frase: ")).lower()
#palabras = palabra.split()
#palabras_unicas = set(palabras)
#recuento = {}
#for i in palabras:
#    recuento[i] = recuento.get(i,0) + 1

#print(palabras_unicas)
#print(recuento)


#Ejercicio 6
#alumnos = {}

#for i in range(1,3):
#    nombre = str(input(f"Ingresa el nombre {i}: "))
#    nota1 = int(input(f"Ingrese la nota 1 de {nombre}:  "))
#    nota2 = int(input(f"Ingrese la nota 2 de {nombre}:  "))
#    nota3 = int(input(f"Ingrese la nota 3 de {nombre}:  "))
#    notas = (nota1,nota2,nota3)
#    alumnos[nombre] = notas
#print(alumnos)


#Ejercicio 7
#parcial1 = {"Ana", "Juan", "Maria", "Luis", "Sofia", "Carlos"}
#parcial2 = {"Juan", "Pedro", "Laura", "Luis", "Ana", "Marta"}

#ambos_parciales = parcial1 & parcial2
#print(f"Aprobaron AMBOS parciales: {ambos_parciales}")

#solo_un_parcial = parcial1 ^ parcial2
#print(f"Aprobaron SOLO UN parcial: {solo_un_parcial}")

#total_aprobados = parcial1 | parcial2
#print(f"Total de alumnos que aprobaron (al menos uno): {total_aprobados}")

#Ejercicio 8
#inventario = {
#    'manzanas': 100,
#    'bananas': 150,
#    'peras': 75
#}

#while True:
#    print("\n--- Sistema de Gestión de Stock ---")
#    print("1. Consultar stock de un producto")
#    print("2. Agregar producto / Añadir stock")
#    print("3. Ver inventario completo")
#    print("4. Salir")
#    
#    opcion = input("Seleccione una opción (1-4): ")

#    if opcion == '1':
#        producto = input("Ingrese el nombre del producto a consultar: ").lower()
#        stock_actual = inventario.get(producto)
#        
#        if stock_actual is not None:
#            print(f"Hay {stock_actual} unidades de {producto}.")
#        else:
#            print(f"El producto '{producto}' no se encuentra en el inventario.")

#    elif opcion == '2':
#        producto = input("Ingrese el nombre del producto: ").lower()
#        cantidad = int(input(f"¿Cuántas unidades de {producto} desea agregar?: "))
#        
#        if cantidad < 0:
#            print("Error: No puede agregar una cantidad negativa.")
#            continue 

#        stock_previo = inventario.get(producto, 0)
#        inventario[producto] = stock_previo + cantidad
#        
#        if stock_previo == 0:
#            print(f"¡Nuevo producto agregado! Stock de {producto}: {inventario[producto]} unidades.")
#        else:
#            print(f"Stock actualizado. Stock de {producto}: {inventario[producto]} unidades.")

#    elif opcion == '3':
#        print("\n--- Inventario Actual ---")
#        if not inventario:
#            print("El inventario está vacío.")
#        else:
#            for producto, stock in inventario.items():
#                print(f"- {producto.capitalize()}: {stock} unidades")

#    elif opcion == '4':
#        print("Saliendo del programa...")
#        break 

#    else:
#        print("Opción no válida. Por favor, elija del 1 al 4.")

#Ejercicio 9
agenda = {}

agenda[('Lunes', '09:00')] = "Reunión de equipo"
agenda[('Martes', '11:00')] = "Turno con el dentista"
agenda[('Miércoles', '18:00')] = "Clase de Python"
agenda[('Viernes', '21:00')] = "Cena con amigos"

evento_lunes = agenda.get(('Lunes', '09:00'))
print(f"El evento del Lunes a las 09:00 es: {evento_lunes}")

print("\n--- Agenda Completa ---")
print(agenda)

#Ejercicio 10