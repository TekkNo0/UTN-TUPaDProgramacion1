titulo = []
ejemplares = []
menu = True
while menu:
    print("\n\t------- MENÚ -------")
    print("(1) Ingresar lista de títulos")
    print("(2) Ingresar ejemplares por título")
    print("(3) Mostrar catálogo con stock")
    print("(4) Consultar disponibilidad de un título")
    print("(5) Listar agotados")
    print("(6) Agregar título")
    print("(7) Ver títulos agotados")
    print("(8) Actualizar ejemplares (préstamo/devolución)")
    print("(9) Ver catálogo")
    print("(10) Salir\n")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        cant = int(input("¿Cuántos libros va a ingresar?: "))
        for i in range(cant):
            titulo_usuario = input(f"Ingrese el título {i+1}: ").lower()
            titulo.append(titulo_usuario)
            ejemplares.append(0)  
        print("Títulos ingresados.\n")
    elif opcion == 2:
        if not titulo:
            print("Primero debe ingresar títulos.\n")
        else:
            titulo_usuario = input("Ingrese el título del libro: ").lower()
            if titulo_usuario in titulo:
                posicion = titulo.index(titulo_usuario)
                ejemplares_usuario = int(input("Ingrese la cantidad de ejemplares: "))
                ejemplares[posicion] = ejemplares_usuario
                print(f"Se asignaron {ejemplares_usuario} ejemplares a '{titulo_usuario}'.\n")
            else:
                print("El título no existe en el catálogo.\n")
    elif opcion == 3:
        print("\n--- CATÁLOGO CON STOCK ---")
        for i in range(len(titulo)):
            if ejemplares[i] > 0:
                print(f"{titulo[i]}: {ejemplares[i]} copia/s")
        print("")
    elif opcion == 4:
        titulo_usuario = input("Ingrese el libro a consultar: ").lower()
        if titulo_usuario in titulo:
            posicion = titulo.index(titulo_usuario)
            print(f"'{titulo[posicion]}' tiene {ejemplares[posicion]} copia/s disponibles.\n")
        else:
            print("El libro no se encuentra en el catálogo.\n")
    elif opcion == 5 or opcion == 7:  
        print("\n--- LIBROS AGOTADOS ---")
        agotados = False
        for i in range(len(titulo)):
            if ejemplares[i] == 0:
                print(f"{titulo[i]} (sin copias)")
                agotados = True
        if not agotados:
            print("No hay libros agotados.\n")
    elif opcion == 6:
        titulo_usuario = input("Ingrese el nuevo título: ").lower()
        ejemplares_usuario = int(input("Ingrese la cantidad de ejemplares: "))
        titulo.append(titulo_usuario)
        ejemplares.append(ejemplares_usuario)
        print(f"Se agregó '{titulo_usuario}' con {ejemplares_usuario} ejemplares.\n")
    elif opcion == 8:
        print("\t(1) Devolución")
        print("\t(2) Préstamo")
        sub_opcion = int(input("Ingrese la opción deseada: "))
        titulo_usuario = input("Ingrese el título del libro: ").lower()
        if titulo_usuario in titulo:
            posicion = titulo.index(titulo_usuario)
            if sub_opcion == 1:
                ejemplares[posicion] += 1
                print(f"Se devolvió una copia de '{titulo[posicion]}'. Ahora hay {ejemplares[posicion]}.\n")
            elif sub_opcion == 2:
                if ejemplares[posicion] > 0:
                    ejemplares[posicion] -= 1
                    print(f"Se prestó una copia de '{titulo[posicion]}'. Ahora hay {ejemplares[posicion]}.\n")
                else:
                    print(f"No hay copias disponibles de '{titulo[posicion]}'.\n")
            else:
                print("Opción inválida.\n")
        else:
            print("El título no existe en el catálogo.\n")
    elif opcion == 9:
        print("\n--- CATÁLOGO COMPLETO ---")
        for i in range(len(titulo)):
            print(f"{titulo[i]}: {ejemplares[i]} copia/s")
        print("")
    elif opcion == 10:
        print("Saliendo del sistema...")
        menu = False
    else:
        print("Opción inválida. Intente de nuevo.\n")
