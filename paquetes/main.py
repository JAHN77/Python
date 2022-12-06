
import my_paquete .aritmetica as a

def main():
    sumar=a.sumar(4,4,5,8,7,9)
    resta=a.restar(10,5)
    potencia=a.potencia(3,3)

    print("La suma es:",sumar)
    print("La resta es:",resta)
    print("La potencia es:",potencia)


if __name__=='__main__':
    main()
