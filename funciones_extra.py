from operaciones import Operaciones

class FuncionesExtra(Operaciones):
    def __init__(self):
        super().__init__()
        
    def multiplicar(self,a, b):
        return a * b
    
    def dividir(self,a, b):
        if b == 0:
            return "no se puede didivir por cero"
        return a / b