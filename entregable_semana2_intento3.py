Calificaciones = []
aprobado=[]
reprobado=[]
Calificaciones.append(aprobado)
Calificaciones.append(reprobado)

def aprobado_reprobado(prompt):
    while(True):
        try:
            variable = float(input(prompt))
            a = variable >= 0 and variable < 60
            if a:
                reprobado.append(variable)
            elif a >=60 and a <=100
                aprobado.append(variable)  
            else:
                print('Numero invalido, elige un numero del 0 al 100')
        except ValueError:
            print('Numero invalido, elige un numero del 0 al 100')

        