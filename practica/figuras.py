#rectanfulo,circulo,funcion probar figura


class Figura:
    __nombre=None

    def __init__(self,nombre,base,altura):
        self.nombre=nombre
        self.base=base
        self.altura=altura
        
    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura):

    def __init__(self,nombre,base,altura):
        self.nombre=nombre
        self.base=base
        self.altura=altura

    def Area(self):
        area=self.base * self.altura
        print(f'El area del Rectangulo es= {area}')
    
    def Perimetro(self):
        perimetro=((self.base**2)+(self.altura**2))
        print(f'El perimetro del Rectangulo es= {perimetro}')


    


# class Circulo:



# class Probar:
