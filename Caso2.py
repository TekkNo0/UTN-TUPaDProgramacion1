menu = True
especialidades = []
cupos = []

while menu:
    print("\t---------MENU---------")
    print("(1)->Ingresar lista de especialidades ")
    print("(2)->Ingresar lista de cupos disponibles por especiaidad ")
    print("(3)->Mostrar agenda")
    print("(4)->Consultar cupos de una especialidad")
    print("(5)->Listar especialidades sin cupo")    
    print("(6)->Agregar especialidad")    
    print("(7)->Ver sin cupo")    
    print("(8)->Actualizar cupos (reservar/cancelar)")    
    print("(9)->Ver agenda")    
    print("(10)->Salir \n")    
    opcion = int(input("Ingrese la opción deseada: "))
    print("")
    if opcion == 1:
        cant = int(input("Cantidad de especialidades a ingresar: "))
        for i in range(0,cant):
            especialidades_usuario = str(input(f"Ingresa la especialidad {i+1} ")).lower()
            especialidades.append(especialidades_usuario)
            cupos.append(0)
    elif opcion == 2:
        if not especialidades:
            print("Primero debes ingresar la especialidad\n")
        else:
            for i in range(0,len(especialidades)):
                cupos_usuario = int(input("Ingresa la cantidad de cupos de las especialidades: "))
                cupos[i] = cupos_usuario
    elif opcion == 3 or opcion == 9:
        print("\t ---------AGENDA---------")
        for i in range(0,len(especialidades)):
            print(f"{especialidades[i]}: {cupos[i]} cupo/s")
    elif opcion == 4:
        especialidades_usuario = str(input("Ingresa la especialidad a consultar: "))
        if especialidades_usuario in especialidades:
            posicion = especialidades.index(especialidades_usuario)
            print(f"{especialidades[posicion]}, {cupos[posicion]} cupo/s \n")
    elif opcion == 5 or opcion == 7:
        print("Especialidades sin cupos")
        for i in range(0,len(especialidades)):
            if cupos[i] == 0:
                print(f"{especialidades[i]}, {cupos[i]} cupo/s")
        print("\n")
    elif opcion == 6:
        especialidades_usuario=str(input("Ingresa la nueva especialidad a la lista: "))
        cupos_usuario = int(input("Ingresa la cantidad de cupos de esta especialidad: "))
        especialidades.append(especialidades_usuario)
        cupos.append(cupos_usuario)
        print("\n")
    elif opcion == 8:
        print("(1)->Reservar \n(2)->Cancelar")
        sub_opcion = int(input("Ingresa la opción deseada: "))
        especialidades_usuario = str(input("Escriba la especialidad: "))
        if especialidades_usuario in especialidades:
            posicion = especialidades.index(especialidades_usuario)
            if sub_opcion == 2:
                cupos[posicion] += 1
                print("Se canceló el cupo.")
            elif sub_opcion == 1:
                if cupos[posicion] > 0:
                    cupos[posicion] -= 1
                    print("Se reservo el cupo")
                else:
                    print("No hay cupos disponibles")    
            else:
                print("Opción invalida\n")
        else:
            print("Especialidad mal ingresada.")
    elif opcion == 10:
        print("Programa finalizado.")
        menu = False