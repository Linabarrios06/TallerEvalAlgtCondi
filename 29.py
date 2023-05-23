#Se debe validar tres atajos de visual estudio code si cumple los tres, deberá informar al usuario que felicidades es correcto de lo contrario debe indicar que no aplica.

listCommands = ["Ctrl+B","Alt+Z","Crtl+K Ctrl+C","Crtl+P","Crtl+,","Ctrl+Enter","Ctrl+V","Ctrl+Z","TAB","Shift+TAB","Ctrl+A"]
#Atajos de visual code 
print(f"These are some Visual Code commands: {listCommands}") #Estos son algunos comandos de Visual Code

def commands (command1,command2,command3):
    
    if command1 == "Ctrl+B" or command1 == "Alt+Z" or command1 == "Ctrl+K" or command1 == "Ctrl+C" or command1 == "Ctrl+P" or command1 == "Ctrl+," or command1 == "Ctrl+Enter" or command1 == "Ctrl+C" or command1 == "Ctrl+V" or command1 == "Ctrl+Z" or command1 == "TAB" or command1 == "Shift+TAB" or command1 == "Ctrl+A":
        print("prueba1")
        
    elif command2 == "Ctrl+B" or command2 == "Alt+Z" or command2 == "Ctrl+K" or command2 == "Ctrl+C" or command2 == "Ctrl+P" or command2 == "Ctrl+," or command2 == "Ctrl+Enter" or command2 == "Ctrl+C" or command2 == "Ctrl+V" or command2 == "Ctrl+Z" or command2 == "TAB" or command2 == "Shift+TAB" or command2 == "Ctrl+A":
        print("prueba2")
        
    elif command3 == "Ctrl+B" or command3 == "Alt+Z" or command3 == "Ctrl+K" or command3 == "Ctrl+C" or command3 == "Ctrl+P" or command3 == "Ctrl+," or command3 == "Ctrl+Enter" or command3 == "Ctrl+C" or command3 == "Ctrl+V" or command3 == "Ctrl+Z" or command3 == "TAB" or command3 == "Shift+TAB" or command3 == "Ctrl+A":
        print("prueba3")
        
    else:
        print("Not applicable") #No aplica


commands(command1=input("Insert a command: "),command2=input("Insert another command: "),command3=input("Insert another command: ")) #1Insertar un comando, #2Insertar otro comando, #3Insertar otro comando