
c=0
suma=0
while c<3:
    try:
        n=int(input('Ingrese un numero:'))
        suma+=n
        c+=1
    except:
        print ("Error: Ingrese solo numerose nteros")
    else:
        print("Funciona todo corectamente")
    finally:
        print("Fin de la ejecucion")

print('la suma total es :', suma)
