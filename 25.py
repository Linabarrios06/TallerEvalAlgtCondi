#25. Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:
# a. ¿Puede volar?
# b. ¿Es humano?
# c. ¿Tiene máscara?

listOfCharacters = ["Spider Man","Doctor Strange","Thor","Hulk","Antman"]

def guess (quest1, quest2, quest3):

    if quest1 == "yes": #si
        
        if quest2 == "yes": #si
                
            if quest3 == "no": 
                print(f"Your characters can be: {listOfCharacters[1]}") #sus personajes pueden ser
            
        elif quest2 == "no":
                
            if quest3 == "no":
                print(f"Your characters can be: {listOfCharacters[2]}") #sus personajes pueden ser
            
    elif quest1 == "no":
        
        if quest2 == "yes":
            
            if quest3 == "yes":
                print(f"Your characters can be: {listOfCharacters[0,4]}") #sus personajes pueden ser
                
            elif quest3 == "no":
                print(f"Your characters can be: {listOfCharacters[3]}") #sus personajes pueden ser
        
    else:
        print("This character is not in the current list") #Este carácter no está en la lista actual
    
print("Please answer yes or no to the following questions") #Responda sí o no a las siguientes preguntas
guess(quest1=input("Can it fly ?: "), quest2=input("It is human?: "), quest3=input("Does it have a mask?: ")) #1¿Puede volar?, #2Es humano, #3¿Tiene máscara?