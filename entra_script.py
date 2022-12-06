import sys

if len(sys.argv)==3:
    textos= sys.argv[1]
    cantidad=int(sys.argv[2])

    c=0
    while c<cantidad:
        print(textos)
        c+=1
else:
    print("error, al ingresar los argumentos correctamente")
    print("ejemplo: entra_script.py 'textos' 5 ")
# print (sys.argv)
