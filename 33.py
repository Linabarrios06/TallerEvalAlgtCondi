#Indicar si entre dos números si ambos son pares o uno de ellos cual es par.

def compare (num1,num2):
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(f"The numbers {num1} and {num2} are pairs") #Los números {} y {} son pares
        
    elif num1 % 2 == 0:
        print(f"Number {num1} is even and number {num2} is odd") #El número {} es par y el número {} es impar
    
    elif num2 % 2 == 0:
        print(f"Number {num2} is odd and number {num1} is ever") #El número {} es impar y el número {} es siempre
    
    else:
        print(f"The numbers {num1} adn {num2} are odd") #Los números {} y {} son impares

compare(num1=int(input("Insert a number: ")),num2=int(input("Insert another number: "))) #1Introduzca un numer, #2Introduzca otro numero