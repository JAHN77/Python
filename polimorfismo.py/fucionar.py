class A:
    def _init_(self):
            print('Soy Clase A')
    def a(self):
            print("Soy método de A")
class B:
    def _init_(self):
            print('Soy Clase B')

class C(A,B):
    def c(self):
        print('Soy metodo de B')

    def a(self):
        print("Soy método de B")

c1=C()
c1.a()
c1.b()
c1.c()

