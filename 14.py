#Un trabajador necesita calcular su salario semanal, el cual se obtiene de la
#siguiente manera: si trabaja 20 horas o menos se le paga $10.000 por hora; si
#trabaja más de 20 horas se le paga $35.000 por hora.

name = input("Insert your name: ") #Introduzca su nombre
hours = int(input("Insert the number of hours worked: ")) #Introduzca el número de horas trabajadas

if hours >= 30:
    salary1 = hours * 35000
    print(f"Your salary is: {salary1}") #Su salario es
    
else:
    salary2 = hours * 10000
    print(f"Your salary is: {salary2}") #Su salario es 
