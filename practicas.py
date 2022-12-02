# palabras palindromas

# revertir=lambda cadena:cadena[::-1]
# a=(input('ingresar palabra:'))
# if a==revertir(a):
#     print('esta palabra es palindroma')
# else:
#     print("esta palabra no es palindroma")


# como lo hizo el profesor

# def palindromo(palabra):
#     palabra=palabra.replace(' ', '')
#     palabra=palabra.lower()
#     palabra_invertida=palabra[::-1]
#     if palabra==palabra_invertida:
#         return True
#     else:
#         return False
    
# def main():
#     palabra=input('ingrese la palabra:')
#     es_palindromo=palindromo(palabra)
#     if es_palindromo:
#         print('Es palindromo')
#     else:
#         print('No es palindroma')

# if __name__=='__main__':
#     main()



# Numeros primos

# def es_primo(numero):
#     contador=0
#     for i in range(1, numero+1):
#         if i == 1 or i==numero:
#             continue
#         if numero % i==0:
#             contador+=1
#     if contador==0:
#         return True
#     else:
#         return False

# def main():
#     numero=int(input('ingrese un numero:'))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')
# if __name__=='__main__':
#     main()

#Generar contraseña
# import random
# def generar_contrasena():
#     mayusculas=['A','B','C','D','E','F','G']
#     minusculas=['a','b','c','d','e','f','g']
#     simbolos=['#','$','%','&']
#     numeros=['1','2','3','4','5','6','7','8','9','0']

#     caracteres=mayusculas+minusculas+simbolos+numeros
#     contrasena=[]

#     for i in range(0,15):
#         caracter_random=random.choice(caracteres)
#         contrasena.append(caracter_random)
    
#     contrasena="".join(contrasena)
#     return contrasena

# def main():
#     contrasena= generar_contrasena()
#     print('Tu nueva contraseña es:', contrasena)

# if __name__=='__main__':
#     main()

#convertidor de moneda 
# def convertir(valor_dolar,pais):
#     cantidad_moneda=float(input(f'ingrese cantidad de {pais}:'))
#     dolares=cantidad_moneda/valor_dolar
#     dolares=round(dolares,2)
#     print(f'tienes ${dolares} Dolares')

# def main():

#     while True:
#         menu=""""
#         1-soles peruanos a dolares
#         2-pesos mexicanos a dolares
#         3-pesos colombianos a dolares
#         4-salir
#         """
#         opcion=input(menu)

#         if opcion=="1":
#             convertir(3.61, 'soles peruanos')
#         elif opcion=="2":
#             convertir(20, 'pesos mexicanos')
#         elif opcion=="3":
#             convertir(3471.27, 'pesos colombianos')
#         elif opcion=="4":
#             print("cerrando conversor de monedas")
#             break
#         else:
#             print("opcion incorrecta!!!")
#             print("vuelve a ingrear la opcion correcta")

# if __name__=='__main__':
#     main()

#juego
import random
def jugar(vidas):
    numero_random=random.randint(1,100)
    numero_elegido=None

    while numero_random!=numero_elegido:
        numero_elegido=int(input('ingrese un numero entre 1 y 100:'))
        
        if numero_random<numero_elegido:
            print('elige un numero mas pequeño')
            vidas-=1
        elif numero_random>numero_elegido:
            print('elige un numero mas grande')
            vidas-=1
        if vidas==0:
            print ('GAME OVER')
            break
        print(f'te quedan {vidas} vidas')
    if numero_elegido==numero_random:
        print("FELICIDADES GANASTES")
def main():
    while True:
        menu=""" 
        ADIVINA EL NUMERO ALEATORIO
        1-Nivel facil
        2-Nivel intermedio
        3-Nivel dificil
        4-salir
        INGRESAR UNA OPCION: """

        opcion=input(menu)

        if opcion=="1":
            jugar(10)
        elif opcion=="2":
            jugar(7)
        elif opcion=="3":
            jugar(5)
        elif opcion=="4":
            print("CERRANDO JUEGO")
            break
        else:
            print("opcion incorrecta vuelve a ingresar")
        

if __name__=='__main__':
    main()