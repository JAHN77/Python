divi=0
try:
    a=int(input("Ingrese el dividendo:"))
    b=int(input("Ingrese el divisor:"))
    divi=a/b
except ValueError:
    print("Error: Ingrese solo numero enteros!")
except ZeroDivisionError:
    print("Error: No se puede dividir por 0")
except Exception as error:
    print("Ha ocurrido error no previsto:", type(error).__name__)

print("la division es:", divi)

