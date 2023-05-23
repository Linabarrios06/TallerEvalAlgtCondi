#Escriba un programa en Python que acepte la opción de dos jugadoras en
# a. Piedra-Papel-Tijera y decida el resultado (solución).
# b. Entrada: persona1=piedra; persona2=papel
# c. Salida: Gana persona2: El papel envuelve a la piedra

jug1=input("Digite su respuesta: Piedra(pi) Papel (pa) Tijera(ti)\n")
jug2=input("Digite su respuesta: Piedra(pi) Papel (pa) Tijera(ti)\n")

if jug1.upper() == "pa" and jug2.upper == "pi": 
    print("Gana el jugador 1") 
elif jug1.upper() == "pi" and jug2.upper == "pa": 
    print("Gana el jugador 2") 
elif jug1.upper() == "pa" and jug2.upper == "ti":
    print("Gana el jugador 2")
elif jug1.upper() == "ti" and jug2.upper == "pa":
    print("Gana el jugador 1")  
elif jug1.upper() == "ti" and jug2.upper == "pi":
    print("Gana eljugador 2")
elif jug1.upper() == "pi" and jug2.upper == "ti":
    print("Gana eljugador 1")

