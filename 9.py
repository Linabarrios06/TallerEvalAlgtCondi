#Determinar si un aprendiz aprueba o reprueba una formación, sabiendo que
#aprobara si su promedio de tres calificaciones es mayor o igual a 10;
#reprueba en caso contrario.

name = input("Insert your name: ") #Introduzca su nombre
formation = input("Insert the name of the formation: ") #Introduzca el nombre de la formación
not1 = int(input("Insert note 1: ")) #Insertar nota 1
not2 = int(input("Insert note 2: ")) #Insertar nota 2
not3 = int(input("Insert note 3: ")) #Insertar nota 3
average = (not1 + not2 + not3)/3

if average >= 10:
    print("You have passed the training") #Ha superado la formación
    
else:
    print("You have not passed the training") #No ha superado la formación