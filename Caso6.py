shows = []
entradas = []
menu = True
while menu:
    print("----MENU----") 
    print("(1)->Ingresar Shows") 
    print("(2)->Ingresar entrada por show") 
    print("(3)->Mostrar shows / entradas") 
    print("(4)->Consultar entradas de un show") 
    print("(5)->Listar shows agotados") 
    print("(6)->Agregar show") 
    print("(7)->Ver agotados") 
    print("(8)->Actualizar entradas(vender/devolución)") 
    print("(9)->Ver todos los shows") 
    print("(10)->Salir\n")
    opcion = input("Ingrese una opcion: ")
    if not opcion.isdigit():
        print("Se espera recibir un numero")
        continue
    opcion = int(opcion) 
    if opcion == 1:
        cant = input("Ingrese la cantidad de shows programados: ")
        if not cant.isdigit():
            print("Se esperaba un numero")
            continue
        cant = int(cant)
        for i in range(0,cant):
            shows_usuario = input("Ingrese los shows programados: ").capitalize()
            if shows_usuario > "@" and shows_usuario < "{" and shows_usuario not in shows:
                shows.append(shows_usuario)
                entradas.append(0)
            else:
                print("Nombre incorrecto")
    elif opcion == 2:
        if not shows:
            print("Pimero haz la opción 1")
        else:
            for i in range(0,len(shows)):
                entradas_usuario = input(f"Ingresa la entrada del show {shows[i]}: ")
                if not entradas_usuario.isdigit():
                    print("Incorrecto")
                    continue
                entradas_usuario = int(entradas_usuario)
                if entradas_usuario < 0:
                    print("Incorrecto")
                    continue
                entradas[i] = entradas_usuario
    elif opcion == 3 or opcion == 9:
        if not shows:
            print("Primero haz la opción 1")
        else:
            for i in range(0,len(shows)):
                print(f"Show: {shows[i]}, entradas: {entradas[i]}")
    elif opcion == 4:
        if not shows:
            print("Primero haz la opción 1.")
        else:
            print("SHOWS:")
            for i in range(0,len(shows)):
                print(f"{shows[i]}")
            show_consulta = input("Ingrese el show a consultar: ")
            if show_consulta.capitalize() in shows:
                for j in range(0,len(shows)):
                    if show_consulta.capitalize() == shows[j]:
                        print(f"SHOW: {shows[j]}, entradas: {entradas[j]}")
            else:
                print("Show no encontrado.")
    elif opcion == 7:
        if not shows:
            print("Primero haz la opción 1")
        else:
            for i in range(0,len(shows)):
                if entradas[i] == 0:
                    print(f"SHOW: {shows[i]}, entradas: {entradas[i]}")
    elif opcion == 8:
        if not shows:
            print("Primero haz la opción 1")
        else:
            print("(1)-> Venta de entradas \n(2)-> Devolución de entradas")
            sub_opcion = input("Ingrese una opción: ")
            if not sub_opcion.isdigit():
                print("Se esperaba un numero")
                continue
            sub_opcion = int(sub_opcion)
            if sub_opcion == 1:
                cant_ventas = input("Ingrese cuantas entradas se venden: ")
                if not cant_ventas.isdigit():
                    print("Se esperaba un numero.")
                    continue
                cant_ventas = int(cant_ventas)
                print("SHOWS:")
                for i in range(0,len(shows)):
                    print(shows[i])
                show_consulta = input("Ingrese el show correspondiente: ")
                if show_consulta.capitalize() in shows:
                    for j in range(0,len(shows)):
                        if show_consulta.capitalize() == shows[j]:
                            if entradas[j] - cant_ventas < 0:
                                print("No hay tantas entradas para vender")
                            else:
                                entradas[j] -= cant_ventas
                                print("Entradas vendidas correctamente.")
                else:
                    print("Show no encontrado.")
            elif sub_opcion == 2:
                cant_devolucion = input("Ingrese cuantas entradas se devuelven: ")
                if not cant_devolucion.isdigit():
                    print("Se esperaba un numero.")
                    continue
                cant_devolucion = int(cant_devolucion)
                for i in range(0,len(shows)):
                    print(shows[i])
                show_consulta = input("Ingrese el show correspondiente: ")
                if show_consulta.capitalize() in shows:
                    for j in range(0,len(shows)):
                        if show_consulta.capitalize() == shows[j]:
                            entradas[j] += cant_devolucion
                            print("Entradas devueltas correctamente")
    elif opcion == 10:
        print("Saliendo...")
        break