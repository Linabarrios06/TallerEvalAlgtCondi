#La oficina de incorporación del ejercito necesita un algoritmo que le pueda permitir saber si un aspirante a ingresar a la institución como soldado es apto o no para poder vincularlo. Para que una persona sea apta, debe cumplir los siguientes requisitos:
#a. Si es mujer, su estatura debe ser superior a 1.60 más y su edad debe estar entre 20 y 25 años.
#b. Si el aspirante es hombre, se estatura debe ser superior a 1.65 más y su edad debe estar entre los 18 y 24 años.
#c. Tanto mujeres como hombres deben ser solteros.
#Diseñe el algoritmo de tal forma que permita informar si un aspirante es apto o no para ingresar al ejército.

print("\nWelcome, to join the army, fill out the form below .") #Bienvenido, para formar parte del ejército, llene el siguiente formulario 
name = input("\nInsert your name: ") #Introduzca su nombre 

def applicant (gender, years, stature, civilStatus):
    
    if gender == "male" and years >= 18 and stature >= 1.65 and civilStatus == "single":
        print(f"\n{name} you are eligible to join the army") #eres apto para ingresar en el ejército
    
    elif gender == "female" and years >= 20 and stature >= 1.60 and civilStatus == "single":
        print(f"\n{name} you are eligible to join the army") #eres apto para ingresar en el ejército
        
    else:
        print(f"\n{name} you are not eligible to join the military.") #no eres apto para ingresar en el ejército
    
applicant(gender = input("Insert your gender female or male: "),years = int(input("Insert your years: ")), stature = float(input("Insert yot stature: ")),civilStatus=input("Insert your marital status, single or married: ")) #1Introduzca su sexo femenino o masculino, #2Introduzca sus años, #3Introduzcza su estatura, #4Inserta tu estado civil, solter@ o casad@ 