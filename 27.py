#Realice un menú donde el usuario deberá seleccionar una opción de las operaciones básicas, y se le solicite al usuario digitar dos números, y dependiendo de la respuesta realice cada operación.

def cal (selectOption,num1,num2):
    
    if selectOption == 1:
        result1 = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result1}") #La suma de {} y {} es

    elif selectOption == 2:
        result2 = num1 - num2
        print(f"The subtract of {num1} and {num2} is: {result2}") #La resta de {} y {} es
    elif selectOption == 3:
        result3 = num1 * num2
        print(f"The multiplication of {num1} and {num2} is: {result3}") #La multiplicaciòn de {} y {} es
        
    elif selectOption == 4:
        result4 = num1 / num2
        print(f"The division of {num1} and {num2} is: {result4}") #La divisiòn de {} y {} es
        
    elif selectOption == 5:
        result5 = num1 // num2
        print(f"The whole division of {num1} and {num2} is: {result5}") #La división entera de {} y {} es
        
    elif selectOption == 6:
        result6 = num1 % num2
        print(f"The quotient of {num1} and {num2} is: {result6}") #El cociente de {} y {} es
        
    else:
        print("This type of operation is not available at this time. .") #Este tipo de operación no está disponible en este momento 

#Calculadora de operaciones básicas
print(f"Basic operations calculator\nSum = 1\nSubtract = 2\nMultiplication = 3\nDivision = 4\nWhole Division = 5\nQuotient = 6\n")
cal(selectOption = int(input("Select a one option: ")), num1 = int(input("Insert a number: ")), num2 = int(input("Insert another number: "))) 
#Seleccione una opción 
#Insertar un número
#Inserte otro nùmero 