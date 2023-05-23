#Diseñe un algoritmo que lea el nombre del estudiante, el valor de su
#matrícula en un curso que responda si¿ Es egresado de la universidad?, si la
#respuesta es SI, se le aplica un 30 % descuento. Muestre el nombre del
#estudiante y el valor de la matricula a pagar.

name = input("Insert your name: ") #Introduzca su nombre
valueRegistration = float(input("Insert tuition value: ")) #Introduzca el valor de la matrícula
ask = input("Are you a graduate of the university?: ") #¿Es usted titulado universitario?
subDiscount = valueRegistration * 0.3
discount = valueRegistration - subDiscount

if ask == "YES" or ask == "yes":
    print(f"\n\nName {name}\nValue Registration: {discount}") #Registro de valores

else:
    print(f"\n\nName {name}\nValue Registration: {valueRegistration}") #Registro de valores
