tarjetas = []
saldos = []
menu = True
while menu:
    print("\n--------Menú--------")
    print("(1)->Ingresar numeros de tarjeta")
    print("(2)->Ingresar saldos correspondientes")
    print("(3)->Mostrar todas las tarjetas y saldos")
    print("(4)->Consultar saldo por número")
    print("(5)->Listar saldos negativos o en cero")
    print("(6)->Agregar tarjeta y saldo")
    print("(7)->Ver saldos menores que 0")
    print("(8)->Cargar / debitar saldo")
    print("(9)->Ver todo")
    print("(10)->Salir\n")
    opcion = int(input("Ingresa la opción deseada: "))
    if opcion == 1:
        cant = int(input("Cantidad de tarjetas a ingresar: "))
        for i in range(0,cant):
            tarjetas_usuario = str(input("Ingrese el número de las tarjetas: ")).lower()
            if len(tarjetas_usuario) == 4:
                tarjetas.append(tarjetas_usuario)
                saldos.append(0)
                print("Tarjeta añadida\n")
            else:
                print("Numero de tarjeta mal dado \n")
                break
    elif opcion == 2:
        if not tarjetas:
            print("Primero ingresar las tarjetas.")
        else:
            for i in range(0,len(tarjetas)):
                print(f"tarjeta: {tarjetas[i]}")
                saldos_usuario = int(input("Ingresa el saldo de la tarjeta: "))
                saldos[i] = saldos_usuario
            print("\nSaldo añadido")
    elif opcion == 3 or opcion == 9:
        if not tarjetas:
            print("Primero ingresa las tarjetas")
        else:
            for i in range(0, len(tarjetas)):
                print(f"Tarjeta: {tarjetas[i]}, saldo:${saldos[i]}") 
    elif opcion == 4:
        if not tarjetas:
            print("Primero ingresar las tarjetas")
        else:
            for i in range(0,len(tarjetas)):
                print(f"Tarjeta: {tarjetas[i]}")
            tarjetas_usuario = str(input("Ingrese la tarjeta deseada: ")).lower()
            if tarjetas_usuario in tarjetas:
                posicion = tarjetas.index(tarjetas_usuario)
                print(f"Tarjeta: {tarjetas[posicion]}, saldo: {saldos[posicion]}")
            else:
                print("Numero mal dado")
    elif opcion == 5 or opcion == 7:
        if not tarjetas:
            print("Primero ingresa las tarjetas")
        else:
            for i in range(0,len(tarjetas)):
                if saldos[i] <= 0:
                    print(f"Tarjeta: {tarjetas[i]}, saldo: {saldos[i]}")
                else:
                    print("Ninguna tarjeta sin saldo")
    elif opcion == 6:
        tarjetas_usuario = str(input("Ingresa el numero de la nueva tarjeta: ")).lower()
        saldos_usuario = int(input("Ingresa el saldo de la nueva tarjeta: "))
        if len(tarjetas_usuario) == 4:
            tarjetas.append(tarjetas_usuario)
            saldos.append(saldos_usuario)
            print("\nTarjeta y saldo añadidos")
        else:
            print("\nNumero mal dado")
    elif opcion == 8:
        if not tarjetas:
            print("Primero ingresa las tarjetas")
        else:
            print("\n(1)->Cargar \n(2)->Debitar")
            minimo = -1000
            sub_opcion = int(input("Ingresa la opción deseada: "))
            if sub_opcion == 1:
                for i in range(0,len(tarjetas)):
                    print(f"Tarjeta: {tarjetas[i]}")
                posicion = tarjetas.index(tarjetas_usuario)
                tarjetas_usuario = str(input("Ingrese la tarjeta deseada: "))
                monto = int(input("Ingrese el monto que quiere cargar: "))
                saldos[posicion] += monto
                print(f"El nuevo saldo de la tarjeta {tarjetas[posicion]} es ${saldos[posicion]}")
            if sub_opcion == 2:
                for i in range(0,len(tarjetas)):
                    print(f"Tarjeta: {tarjetas[i]}")
                posicion = tarjetas.index(tarjetas_usuario)
                tarjetas_usuario = str(input("Ingrese la tarjeta deseada: "))
                monto = int(input("Ingrese el monto a debitar: "))
                saldos[posicion] -= monto
                if saldos[posicion] >= minimo:
                    print(f"El nuevo saldo de la tarjeta {tarjetas[posicion]} es ${saldos[posicion]}")
                else:
                    print("Saldo insuficiente")    
                    saldos[posicion] += monto
    elif opcion == 10:
        print("Saliendo del sistema...")
        menu = False
    else:
        print("\nOpción mal dada")