
# def sumar(a,b):
#     return a+b

sumar=lambda a,b:a+b
doblar=lambda n:n*2
par=lambda n: n%2==0
imapar=lambda n: n%2!=0
revertir=lambda cadena:cadena[::-1]

print(sumar(10,20))
print(doblar(10))
print(par(5))
print(imapar(5))
print(revertir("hola"))
print("hola mundo".upper())
print("Hola mundo".lower())
print("hola mundo".capitalize())
print("hola mundo".title())
print("hola mundo".count('o'))

palabra='python'
palabra=palabra.replace('P','S')
