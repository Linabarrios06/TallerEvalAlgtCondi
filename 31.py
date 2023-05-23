#Realizar el siguiente algoritmo:
#Calcular el salario de un empleado dado el numero de horas, el valor de la hora y la categoria del empleado
#Categoria - Incremento
#   A           10%
#   B           15%
#   C           23%
#   D           25%

def salary(category,numNours,valueHour):
    subTotal = numNours * valueHour
    
    if category == "A":
        increaseA = subTotal * 0.1
        totalA = subTotal + increaseA
        print(f"Your salary final is: {totalA}") #Su salario final es
    
    elif category == "B":
        increaseB = subTotal * 0.15
        totalB = subTotal + increaseB
        print(f"Your salary final is: {totalB}") #Su salario final es
    
    elif category == "C":
        increaseC = subTotal * 0.23
        totalC = subTotal + increaseC
        print(f"Your salary final is: {totalC}") #Su salario final es
    
    elif category == "D":
        increaseD = subTotal * 0.23
        totalD = subTotal + increaseD
        print(f"Your salary final is: {totalD}") #Su salario final es
        
    else:
        print(f"Error, category {category} does not exist") #Error, categoría {} no existe
    
salary(category=input("Enter the category you belong to \"A,B,C or D\": "),numNours=int(input("Insert number of hours worked: ")),valueHour=int(input("Insert hourly rate: "))) #1Introduzca la categoría a la que pertenece, #2Introduzca el número de horas trabajadas, #3Inserte la tarifa horaria.