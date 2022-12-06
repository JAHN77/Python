from io import open
from os import path
def escribir_archivo():
    archivo= open("texto.txt",'w')
    archivo.write("hola mundo")
    archivo.close()

def leer_archivos():
    if path.isfile("texto.txt"):
        archivo=open('texto.txt','r')
        # textos=archivo.read()
        textos=archivo.readlines()
        archivo.close()

        print(textos)

    else:
        print("el archivo no existe")

def agregar_datos():
    if path.isfile("texto.txt"):
        archivo=open('texto.txt','a')
        # textos=archivo.read()4
        archivo.write('\ncomo fue')
        archivo.close()



    else:
        print("el archivo no existe")

def modificar_datos():
    if path.isfile("texto.txt"):
        archivo=open('texto.txt','r+')
        # textos=archivo.read()
        textos=archivo.readlines()
        print(textos)
        textos[1]='hola alex roel\n'
        # archivo.write("\nHabla")
        print(textos)
        archivo.seek(0)
        archivo.writelines(textos)
        archivo.close()
        print(textos)


    else:
        print("el archivo no existe")

def eliminar_datos():
    if path.isfile("texto.txt"):
        archivo=open('texto.txt','w')
        archivo.close


# leer_archivos()

# escribir_archivo()
# agregar_datos()
# modificar_datos()
# eliminar_datos()