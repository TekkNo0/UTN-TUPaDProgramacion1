clases = []
cupos = []
menu = True
while menu:
    print("\n\t------MENÚ------")
    print("(1)->Ingresar lista de clases")
    print("(2)->Ingresar cupos por clase")
    print("(3)->Mostar clases con cupos")
    print("(4)->Consultar cupo de una clase")
    print("(5)->Listar clases sin cupo")
    print("(6)->Agregrar clase")
    print("(7)->Ver sin cupo")
    print("(8)->Actualizar cupos")
    print("(9)->Ver todas las clases")
    print("(10)->Salir\n")
    opcion = input("Ingresa una opción: ").strip()
    if not opcion.isdigit():
        print("Opcion mal dada")
        continue
    opcion=int(opcion)
    
    if opcion == 1:
        cant = int(input("Ingrese cuantas clases va a sumar a la lista: "))
        for i in range(0,cant):
            clases_usuario = str(input(f"Ingrese la clase {i+1}: ")).lower()
            if clases_usuario > "@" and clases_usuario < "{":
                clases.append(clases_usuario)
                cupos.append(0)
            else:
                print("Nombre incorrecto")
    elif opcion == 2:
        if not clases:
            print("Primero haz la opción 1\n")
        else:            
            for i in range(0,len(clases)):
                print(f"Clase {i+1}: {clases[i]}")
                cupos_usuario = int(input("Ingresa la cantidad de cupos: "))
                cupos[i] = cupos_usuario
    elif opcion == 3:
        if not clases:
            print("Primero haz la opción 1\n")
        else:
            for i in range(0,len(clases)):
                if cupos[i] > 0:
                    print(f"Clase: {clases[i]}, Cupos: {cupos[i]}")
                elif 0 not in cupos:
                    print("Niguna clase tiene cupos")
    elif opcion == 4:
        if not clases:
            print("Primero haz la opción 1\n")
        else:
            for i in range(0,len(clases)):
                print(f"Clases: {clases[i]}")
            clases_usuario = str(input("Ingresa la clase que quiere consultar: ")).lower()
            posicion = clases.index(clases_usuario)
            if clases_usuario in clases:
                print("--------CONSULTA---------\n")
                print(f"Clase: {clases[posicion]}, Cupos: {cupos[posicion]}")
            else:
                print("Clase mal escrita.")
    elif opcion == 5 or opcion == 7:
        if not clases:
            print("Primero haz la opción 1\n")
        else:
            for i in range(0,len(clases)):
                if cupos[i] == 0:
                    print(f"Clase: {clases[i]}, Cupos: {cupos[i]}")
    elif opcion == 6:
        clases_usuario = str(input("Ingresa la nueva clase a la lista: ")).lower()
        if clases_usuario in clases:
            print("Esa clase ya esta agregada")
        else:
            cupos_usuario = int(input("Ingresa los cupos de esa clase: "))
            clases.append(clases_usuario)
            cupos.append(cupos_usuario)
    elif opcion == 8:
        if not clases:
            print("Primero haz la opción 1")
        else:
            print("(1)->Inscribir \n(2)->Baja")
            sub_opcion = int(input("Ingrese la opción deseada: "))
            print(" ")
            for i in range(0,len(clases)):
                print(f"Clase: {clases[i]}")
            clases_usuario = str(input("Ingrese que clase quiere inscribir: "))
            if sub_opcion == 1: 
                if clases_usuario in clases:
                    posicion = clases.index(clases_usuario)
                    if cupos[posicion] > 0:
                        print("\n INSCRIPCIÓN ")
                        print("Alumno Inscripto")
                        cupos[posicion] -= 1
                    else:
                        print("Clase sin cupos")
                else:
                    print("La clase no se encuentra")
            elif sub_opcion == 2:
                if clases_usuario in clases:
                    posicion = clases.index(clases_usuario)
                    print("\n BAJA ")
                    print("Alumno dado de baja")
                    cupos[posicion]  += 1
                else:
                    print("La clase no se encuentra")
            else: 
                print("Vuelve a intentarlo\n")
                
    elif opcion == 9:
        if not clases:
            print("Primero haz la opción 1 \n")
        else:
            for i in range(0,len(clases)):
                print(f"{clases[i]}: {cupos[i]} cupo/s")
    elif opcion == 10:
        print("Saliendo del programa...")
        menu = False
    else:
        print("Opción fuera de rango")