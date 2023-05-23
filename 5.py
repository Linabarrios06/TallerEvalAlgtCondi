#Un hombre desea saber cuánto dinero se genera por concepto de intereses
#en relación la cantidad que tiene en inversión en el banco.

value = float(input("Enter the amount to invest: ")) #Introduzca el importe a invertir

if value <= 7000:
    print("You can reinvest the interest") #You can reinvest the interest
    
else:
    print("You cannot reinvest interest") #No se pueden reinvertir los intereses
    