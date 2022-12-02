
def sumar(*args, **kwargs):
    suma=0
    for n in args:
        suma+=n
    return suma,kwargs



suma_total,datos=sumar(1,2,3,4,5,6,nombre="Alex",eda=25)
print('la suma total es:',suma_total)
print(datos)