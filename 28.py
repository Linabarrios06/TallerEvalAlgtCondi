#La tienda sofia valida el valor de la compra si el valor de la compra es mayor a 40 mil , si es así debe indicar el color de la balota(roja 10%, blanca 15%, negra 20%,amarilla 25%, verde 30%) según el color se aplica el descuento, se debe mostrar el descuento y el valor neto a pagar.
#Si los valores son menores que 40 no va aplicar ningún descuento.

print("\nWelcome to the Sofia warehouse") #Bienvenido al almacén de Sofía

def warehouse (value1):
    
    if value1 >= 40000:
        ballot = input(f"\nChoose a type of ballot, the colors are: red, white, black, yellow and green: ")
        #Elige un tipo de papeleta, los colores son: rojo, blanco, negro, amarillo y verde.
        
        if ballot == "red": #rojo
            subTotalRed = value1 * 0.1
            totalRed = value1 - subTotalRed
            print(f"\nINVOICE\nProduct price: {value1}\nDiscount: {subTotalRed}\nFinal Price: {totalRed}") #1Precio del producto, #2Descuento, #3Precio final
        
        elif ballot == "white":
            subTotalWhite = value1 * 0.15
            totalWhite = value1 - subTotalWhite
            print(f"\nINVOICE\nProduct price: {value1}\nDiscount: {subTotalWhite}\nFinal Price: {totalWhite}") #1Precio del producto, #2Descuento, #3Precio final
        
        elif ballot == "black":
            subTotalBlack = value1 * 0.2
            totalBlack = value1 - subTotalBlack
            print(f"\nINVOICE\nProduct price: {value1}\nDiscount: {subTotalBlack}\nFinal Price: {totalBlack}") #1Precio del producto, #2Descuento, #3Precio final
        
        elif ballot == "yellow":
            subTotalYellow = value1 * 0.25
            totalYellow = value1 - subTotalYellow
            print(f"\nINVOICE\nProduct price: {value1}\nDiscount: {subTotalYellow}\nFinal Price: {totalYellow}") #1Precio del producto, #2Descuento, #3Precio final
        
        elif ballot == "green":
            subTotalGreen = value1 * 0.3
            totalGreen = value1 - subTotalGreen
            print(f"\nINVOICE\nProduct price: {value1}\nDiscount: {subTotalGreen}\nFinal Price: {totalGreen}") #1Precio del producto, #2Descuento, #3Precio final
    
    else:
        print(f"\nINVOICE\nProduct price: {value1}\nDiscount: 0\nFinal Price: {value1}") #1Precio del producto, #2Descuento, #3Precio final
    
warehouse(value1=int(input("\nInsert the quantity of the product value: "))) #Inserte la cantidad del valor del producto