#Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
#Si se compran tres camisas o más se aplica un descuento del 15% sobre el
#total de la compra y si son menos de 3 camisas el descuento es del 5%.

price = int(input("Insert shirt price: ")) #Insertar el precio de la camisa
shirts = int(input("Insert the number of shirts purchased: ")) #Introduzca el número de camisetas compradas

if shirts >= 3:
    subtotal1 = (price * shirts)
    discount1 = subtotal1 * 0.15
    total1 = subtotal1 - discount1
    print(f"The final price is: {total1}") #El precio final es de {}
    
else:
    subtotal2 = (price * shirts)
    discount2 = subtotal2 * 0.05
    total2 = subtotal2 - discount2
    print(f"The final price is: {total2}") #El precio final es de {}

