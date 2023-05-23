#Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
#Si se compran tres camisas o más se aplica un descuento del 15% sobre el
#total de la compra y si son menos de 3 camisas el descuento es del 5%.

value1 = int(input("Insert one side: ")) #Insertar un lado
value2 = int(input("Insert the other side: ")) #Inserte el otro lado 
area = value1 * value2

if area > 10:
    print(f"The area is {area}") #La zona es
    
else:
    print("Does not apply") #No aplicable
    

