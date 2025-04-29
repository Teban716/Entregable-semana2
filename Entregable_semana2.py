def pedir_numero_cero_y_cien(prompt):
    while(True):
        try:
            variable = float(input(prompt))
            es_valido = variable >= 0 and variable <= 100
            if es_valido:
                return variable
            else:
                print('Numero invalido, elige un numero del 0 al 100')
        except ValueError:
            print('Numero invalido, elige un numero del 0 al 100')

estudiantes_aprobados=[]
estudiantes_reprobados=[]
while(True):
    nombre=input("Ingrese el nombre del estudiante:   ")
    calificacion=pedir_numero_cero_y_cien("Ingrese la calificacion entre 0 y 100: ")
    if (calificacion < 60)
        estudiantes_reprobados.append((nombre,calificacion))
    else:
        estudiantes_aprobados.append((nombre,calificacion))
    continuar=input ("Desea añadir otro estudiante?(SI/NO): ").lower()
    if continuar != "si":   
        print ("/nResumen de Calificaciones")
    for nombre,calificacion in Lista_calificaciones:
        print(f"{"Nombre: "}{nombre}:{"Nota: "}{calificacion}")

