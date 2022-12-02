

def saludar(nombre):
    # global nombre
    return f"Hola,{nombre} desde la funcion saludar"

def sumar(a,b):
    return a+b

def restar(a=None,b=None):
    if a==None or b==None:
        print("error: deves enviar dos numeros")
        return
    return a-b

saludo=saludar("roel")
print(saludo)

suma=sumar(10,20)
print("la suma es:",suma)

resta=restar()
print("la resta es:",resta)

# print("hola",nombre)

# def adios():
#     print("adios", nombre)
# adios()