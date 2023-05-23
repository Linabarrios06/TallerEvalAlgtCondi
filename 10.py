#Mostrar la suma de dos números enteros, si el resultado supera a 10

num1 = int(input("Insert a number: ")) #Insertar un número
num2 = int(input("Insert another number: ")) #Insertar otro número
sum = num1 + num2

if sum >= 10:
    print(f"The sum of the numbers is: {sum}") #La suma de los números es
    
else:
    print("\nThe sum of the numbers does not reach the minimum limit to perform the operation.") #La suma de los números no alcanza el límite mínimo para realizar la operación