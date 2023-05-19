#Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso,
#nota definitiva, el nro de clases en el semestre y el número de las fallas. En el
#caso de que las fallas superen el 30% del número de clases se debe mostrar
#la nota que no aprobó y se calificara cero(0)

def Data(Name, CourseName, DefinitiveNote, NamOfClasses , NamOfFailures): 
    """ print(f"\n\nLos Datos del Formulario enviado son:\nName: {Name}\nCourse Name: {CourseName}\nDefinitive note: {DefinitiveNote}\nNumber of classes: {NameOfClasses}\nNumber of failures: {NamOfFailures}")  """

Name = input("Enter your name : ") #Nombres
#Ingrese su nombre
CourseName = input("enter the name of your course: ") #Nombre del curso
#Ingrese el nombre de su curso
DefinitiveNote = int(input("Enter your final grade   : ")) #Nota definitiva
#Ingrese su nota final
NameOfClasses = int(input("Enter the total number of classes in the semester  : ")) #Numero de clases
#Ingrese el numero total de clases en el semestre
NamOfFailures = int(input("Enter the total number of failures : ")) #Numero de fallas
#Ingrese el numero total de fallas 
Note = NameOfClasses * 0.3
Data(Name,CourseName,DefinitiveNote,NameOfClasses, NamOfFailures)

if NamOfFailures <= Note:
    print(f"\nyour current semester information is:  \nName: {Name}\nCourse name: {CourseName}\nDefinitive note: {DefinitiveNote}\nNumber of classes: {NameOfClasses}\nNumber of failures: {NamOfFailures}")

else:
    Note = 0
    print(f"\nyour current semester information is:  \nName: {Name}\nCourse name: {CourseName}\nDefinitive note: {DefinitiveNote}\nNumber of classes: {NameOfClasses}\nNumber of failures: {NamOfFailures}")
 
