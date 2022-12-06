import random

while True:
    menu=("""JUEGO DE PIEDRA, PAPEL O TIJERA:
    1-Piedra
    2-Papel
    3-Tijera
    4-Salir""")
    
    print(menu)

    usuario=int(input("Ingrese una opcion:"))

    if usuario==1:
        usuario="Piedra"
    elif usuario==2:
        usuario="Papel"
    elif usuario==3:
        usuario="Tijera"
    elif usuario==4:
        print('Cerrando...')
        break
    else:
        print("opcion incorrecta")

    eleccion_maquina=random.randint(1,3)
    if eleccion_maquina==1:
        eleccion_maquina="Piedra"
    elif eleccion_maquina==2:
        eleccion_maquina="Papel"
    elif eleccion_maquina==3:
        eleccion_maquina="Tijera"

    print(f"El usuario eligio:{usuario}\nLa maquina eligio:{eleccion_maquina}")
    
    if usuario==eleccion_maquina:
        print("EMPATE")

    elif usuario=="Piedra" and eleccion_maquina=="Papel":
        print("PERDISTE")  
    elif usuario=="Papel" and eleccion_maquina=="Tijera":
        print("PERDISTE")
    elif usuario=="Tijera" and eleccion_maquina=="Piedra":
        print("PERDISTE")

    elif usuario=="Piedra" and eleccion_maquina=="Tijera":
        print("GANASTE!!!")
    elif usuario=="Papel" and eleccion_maquina=="Piedra":
        print("GANASTE!!!")
    elif usuario=="Tijera" and eleccion_maquina=="Papel":
        print("GANASTE!!!")