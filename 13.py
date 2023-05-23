#Dado tres números calcular el menor

def lowerNumber (number1, number2, number3):
    
    if number1 <= number2 and number1 <= number3:
        print(f"{number1} is less than {number2} and {number3}") #es inferior a {} y {}
        
    elif number2 <= number1 and number2 <= number3:
        print(f"{number2} is less than {number1} and {number3}") #es inferior a {} y {}
        
    else:
        print(f"{number3} is less than {number1} and {number2}") #es inferior a {} y {}
        
lowerNumber(number1 = int(input("Insert a number: ")), number2 = int(input("Insert another number: ")), number3 = int(input("Insert another number: "))) #1Insert a number, 2Insertar otro número, 3Insertar otro número