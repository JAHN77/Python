from sys import argv

if len(argv)==4:
    nombre= argv[1]
    edad=int(argv[2])
    altura=float(argv[2])

    # print(f"Nombre:{nombre}\n Edad:{edad}\nAltura:{altura}")
    # print("Nombre:{n}\nEdad:{e}\nAltura:{a}".format(n=nombre,e=edad,a=altura))
    print("Nombre: %s \nEdad: %i \nAltura: %f"%(nombre,edad,altura))


else:
    print("error, al ingresar los argumentos correctamente")
    print("ejemplo: entra_script.py 'textos' 5 ")