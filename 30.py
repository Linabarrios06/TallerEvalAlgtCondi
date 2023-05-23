#Realizar el siguente algoritmo
#Entrada: Un numero que se almacena en una variable llamada numeroDia
#Proceso: Realizar las respectivas comparaciones para cada uno de los valores entre 1 y 7
#Salida: Mostrar el nombre del dia segun el valor contenido en numeroDia

def week (numberDay):
    
    if numberDay == 1:
        print(f"{numberDay} corresponds to Monday") #corresponde a lunes
    
    elif numberDay == 2:
        print(f"{numberDay} corresponds to Tuesday") #corresponde a martes 
    
    elif numberDay == 3:
        print(f"{numberDay} corresponds to Wednesday") #corresponde a miercoles 
    
    elif numberDay == 4:
        print(f"{numberDay} corresponds to Thursday") #corresponde a jueves 
    
    elif numberDay == 5:
        print(f"{numberDay} corresponds to Friday") #corresponde a viernes
    
    elif numberDay == 6:
        print(f"{numberDay} corresponds to Saturday") #corresponde a sabado
    
    elif numberDay == 7:
        print(f"{numberDay} corresponds to Sunday") #corresponde a domingo
        
    else:
        print(f"{numberDay} is not a day of the week") #no es un día de la semana
        
week(numberDay=int(input("Insert a number from 1 to 7: "))) #Introduzca un número del 1 al 7