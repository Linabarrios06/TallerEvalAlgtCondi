#Determinar si un número es par o impar.

num = int(input("Insert a number: ")) #Insertar un número

if num % 2 == 0:
    print(f"{num} It is an even number") #Es un número par
    
else:
    print(f"{num} It is an odd number") #Es un número impar