fecha_actual = str(input("Ingrese la fecha actual (ej: Martes 26 04): "))
fecha_actual = fecha_actual.lower()
fecha_separada = fecha_actual.split()

fecha_dia_semana = fecha_separada[0]
fecha_dia = int(fecha_separada[1])
fecha_mes = int(fecha_separada[-1])
print("Fecha ingresada:",fecha_dia_semana + ",",str(fecha_dia) + "/" + str(fecha_mes))
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

if fecha_dia_semana not in dias or fecha_dia < 1 or fecha_dia > 31 or fecha_mes < 1 or fecha_mes > 12:
    print("Error, no pusiste las fechas bien.")
else:
    if fecha_dia_semana in ["lunes", "martes", "miercoles"]:
        examen = str(input("¿Hubo examen? 1 -> SI / 2 -> NO: ")).lower()
        if examen == "1" or examen == "si":
            alumnos_aprob = int(input("Ingrese la cantidad de alumnos que aprobaron el examen: "))
            alumnos_desaprob = int(input("Ingrese la cantidad de alumnos que desaprobaron el examen: "))
            total = alumnos_aprob + alumnos_desaprob
            porcentaje = alumnos_aprob / total * 100
            print("El porcentaje de alumnos aprobados es de", porcentaje, "%")
        else:
            print("No hubo examen.")


    elif fecha_dia_semana == "jueves":
        asistencia = int(input("Ingrese el porcentaje de alumnos que asistieron: "))
        if asistencia > 50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")


    elif fecha_dia_semana == "viernes":
        if fecha_dia == 1 and (fecha_mes == 1 or fecha_mes == 7):
            print("Nuevo ciclo")
            alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            ingreso = float(input("Ponga el ingreso en $ por cada alumno: "))
            ingreso_total = alumnos * ingreso
            print("El ingreso total es de $", ingreso_total)
        else:
            print("Clase de ingles para viajeros")
