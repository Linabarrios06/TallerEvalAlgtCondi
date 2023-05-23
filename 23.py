#23. Un cliente va a comprar una moto y se percata que si lo compraba el día martes tiene un descuento del 10%, luego si lo compra el día sábado tiene un descuento del 18% mostrar cuanto pagara en cada opción.

valueMotorcycle = int(input("Insert the value of the motorcycle: ")) #Introduzca el valor de la motocicleta
disccountTuesday = valueMotorcycle * 0.1
totalTuesday = valueMotorcycle - disccountTuesday
disccountSaturday = valueMotorcycle * 0.18
totalSaturday = valueMotorcycle - disccountSaturday

def pay (day):
    
    if day == "tuesday" or day == "TUESDAY":
        print(f"The cost of the motorcycle on Tuesday is: {totalTuesday}") #El coste de la motocicleta el martes es de
        
    elif day == "saturday" or day == "SATURDAY":
        print(f"The cost of the motorcycle on Saturday is: {totalSaturday}") #El coste de la moto el sábado es de
    
    else:
        print("No discounts apply on this day") #Este día no se aplican descuentos
        
pay(day=input("Insert day: ")) #Inserte el día