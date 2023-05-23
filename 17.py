#Hacer un programa que pida dos números y los imprima en forma
#ascendente y descendente.

list = []
value1 = int(input("Insert a number: ")) #Insertar un número 
value2 = int(input("Insert another number: ")) #Insertar otro número 

list.append(value1)
list.append(value2)

print(f"\nthe values to add are: {value1} and {value2}") #los valores a añadir son{}y{}
list.sort()

print(f"\nAscending List: {list}") #Lista ascendente

list.reverse()

print(f"\nDescending List: {list}") #Lista descendente