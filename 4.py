#Diseña un algoritmo que lea 2 números y visualice si son positivos.
number1 = int(input("Insert a number: ")) #Introduzca un número
number2 = int(input("Insert another number: ")) #Insertar otro número

if number1 > 0 and number2 > 0:
    print("Both numbers are positive") #Ambas cifras son positivas
    
else:
    print("One or both numbers are negative") #Uno o ambos números son negativos