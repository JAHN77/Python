
def factorial(n):
    print('valor inicial=>', n)
    if n>1:
        n=n*factorial(n-1)
    
    print('calor final=>',n)
    return n

n=int(input('ingrese un numero: '))

f=factorial(n)
print(f'su factorial de {n} es:',f)