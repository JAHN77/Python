class OperadorExepcion(Exception):
    def __init__ (self,mensaje):
        super().__init__(mensaje)


def dividir(a,b):
    if b==0:
        raise OperadorExepcion ("Error:no se puede dividir entre 0")

    else:
        return a/b

dividir(4,0)