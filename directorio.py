nombre=[]
apellido=[]
telefono=[]
ciudad=[]

menu="""DIRECTORIO 
1-Agregar contacto al directorio
2-Eliminar contacto del  directorio
3-salir"""
for i in range(99999):
    print(menu)

    usuario=int(input("Ingrese la opcion que desea ejecutar:"))



    if usuario==1:
        #llena las listas
        for i in range(999999):

            n=input("ingrese nombre:")
            nombre.append(n)
            a=input("ngrese apellido:")
            apellido.append(a)
            t=input("ingrese telefono:")
            telefono.append(t)
            c=input("ingrese ciudad:")
            ciudad.append(c)

            terminar=input("quieres dejar de aregar?(s/n)")    
            if terminar=="s":
                print("Se termino de agregar")
                print("DIRECTORIO")
                directorio=list(zip(nombre,apellido,telefono,ciudad))
                directorio.sort()

                print(directorio)
                break
            elif terminar=="n":
                pass




        
        
    elif usuario==2:
        
        d=int(input("ingrese el espacio que ocupa el valor a eliminar iniciando por 0:"))
        print(directorio,"datos actuales")
        directorio.pop(d)
        print(directorio,"sin los datos eliminados")
        

    elif usuario==3:
        print("Cerrando dierectorio...")
        break

    # directorio=list(zip(nombre,apellido,telefono,ciudad))
    # directorio.sort()
    # # directorio.pop(0)

    # print(directorio)
