#Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso,
#nota definitiva, el nro de clases en el semestre y el número de las fallas. En el
#caso de que las fallas superen el 30% del número de clases se debe mostrar
#la nota que no aprobó y se calificara cero(0)

def Data(name, courseName, definitiveNote, namOfClasses , namOfFailures): 
    """ print(f"\n\nLos Datos del Formulario enviado son:\nName: {Name}\nCourse Name: {CourseName}\nDefinitive note: {DefinitiveNote}\nNumber of classes: {NameOfClasses}\nNumber of failures: {NamOfFailures}")  """

name = input("Enter your name : ") #Nombres
#Ingrese su nombre
courseName = input("enter the name of your course: ") #Nombre del curso
#Ingrese el nombre de su curso
definitiveNote = int(input("Enter your final grade: ")) #Nota definitiva
#Ingrese su nota final
nameOfClasses = int(input("Enter the total number of classes in the semester  : ")) #Numero de clases
#Ingrese el numero total de clases en el semestre
namOfFailures = int(input("Enter the total number of failures : ")) #Numero de fallas
#Ingrese el numero total de fallas 
note = nameOfClasses * 0.3
 
if namOfFailures <= note:
    print(f"\n\nInformacion Semestre: \nName: {name}\nCourse Name: {courseName}\nFinal Note: {note}\nN° Classes: {nameOfClasses}\nN° Fails: {namOfFailures}")
    
else:
    note = 0
    print(f"\n\nInformacion Semestre: \nName: {name}\nCourse: {courseName}\nFinal Note: {note}\nN° Classes: {nameOfClasses}\nN° Fails: {namOfFailures}")
