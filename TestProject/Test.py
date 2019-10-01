class Clase:
    def __init__(self, nombre):
        self.name = nombre
    
    def imprimir(self):
        print("Tu nombre es " + self.name)
    
ejemplo = Clase("Alejandro")
ejemplo.imprimir()