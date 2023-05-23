#Hacer un programa que pida 3 números e indicar si el tercero es igual a la
#suma del primero y el segundo.

num1 = int(input("Insert a number: ")) #Insertar un número
num2 = int(input("Insert another number: ")) #Insertar otro número 
num3 = int(input("Insert another number: ")) #Insertar otro número 
sum = num1 + num2

if num3 == sum:
    print(f"The sum {num1} and {num2} is equal {num3}") #La suma {} y {} es igual {}
    
else:
    print(f"the sum of numbers {num1} and {num2} do not equal {num3}") #la suma de números {} y {} no son iguales