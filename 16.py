# En un Almacén de cadena, se hace una promoción mediante la cual el
#cliente obtiene un descuento dependiendo de un número que se escoge al
#azar, si el número escogido es menor a 65 el descuento es del 20% sobre el
#total de la compra si es mayor o igual a 65 el descuento es del 30%.

product = int(input("Insert product value: ")) #Introduzca el valor del producto
number = int(input("Insert a number: ")) #Insertar un número

if number >= 65:
    discount1 = product * 0.3
    total1 = product - discount1
    print(f"Your number {number} is greater than 65 and you have obtained a 30% discount on your product, the final price is: {total1}") #Su número {} es superior a 65 y ha obtenido un descuento del 30% en su producto, el precio final es de {}
    
else:
    discount2 = product * 0.2
    total2 = product - discount2
    print(f"Your number {number} is less than 65 and you have obtained a 20% discount on your product, the final price is: {total2}") #Su número {}es inferior a 65 y ha obtenido un descuento del 20% en su producto, el precio final es de {}
    
