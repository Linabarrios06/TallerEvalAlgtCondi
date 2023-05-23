#Dado tres números calcular cual es el mayor de los tres.

def lowerNum (num1, num2, num3):
    
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is larger than {num2} and {num3}") #es mayor que {} y {}
        
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is larger than {num1} and {num3}") #es mayor que {} y {}
        
    else:
        print(f"{num3} is larger than {num1} and {num2}") #es mayor que {} y {}
        
lowerNum(num1 = int(input("Insert a number: ")), num2 = int(input("Insert another number: ")), num3 = int(input("Insert another number: "))) #Insertar un número, #Insertar otro número, #Insertar otro número 