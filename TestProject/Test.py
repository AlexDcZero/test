'''class Clase:
    def __init__(self, nombre):
        self.name = nombre
    
    def imprimir(self):
        print("Tu nombre es " + self.name)
    
ejemplo = Clase("Alejandro")
ejemplo.imprimir()'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

cuadrado = Square(2.3)
print(cuadrado.area())