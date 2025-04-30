estudiantes_aprobados=[]
estudiantes_reprobados=[]

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

# def Info_estudiante():
#     nombre=input("Ingrese el nombre del estudiante:   ")
#     calificacion=pedir_numero_cero_y_cien("Ingrese la calificacion entre 0 y 100: ")
#     Organizar={
#         "Nombre":nombre,
#         "Calificacion":calificacion
#     }

#     if (calificacion < 60):
#         estudiantes_reprobados.append(Organizar)
#     else:
#         estudiantes_aprobados.append(Organizar)
while(True):
    nombre=input("Ingrese el nombre del estudiante:   ")
    calificacion=pedir_numero_cero_y_cien("Ingrese la calificacion entre 0 y 100: ")


    if (calificacion < 60):
        Organizar_reprobados={
        "Nombre":nombre,
        "Calificacion":calificacion
        }
        estudiantes_reprobados.append(Organizar_reprobados)
    else:
        Organizar_aprobados={
        "Nombre":nombre,
        "Calificacion":calificacion
        }
        estudiantes_aprobados.append(Organizar_aprobados)

    continuar=input ("Desea añadir otro estudiante?(SI/NO): ").lower()
    while(True):
        try:
            if continuar == ("si"):
                break
            elif continuar==("no"):
                print("---------------------------")
                print ("Resumen de Calificaciones")
                print("---------------------------")
                print("ESTUDIANTES APROBADOS")
                for i in estudiantes_aprobados:
                    print(f'Nombre: {Organizar_aprobados["Nombre"]}{"  "}Calificacion:{Organizar_aprobados["Calificacion"]}')
                print("---------------------------")
                print("ESTUDIANTES REPROBADOS")
                for i in estudiantes_reprobados:
                    print(f'Nombre: {Organizar_reprobados["Nombre"]}{"  "}Calificacion:{Organizar_reprobados["Calificacion"]}')
                break
            else:
                pass
        except ValueError:
            print("Ingresar valor correcto") 
    


        
    
            


