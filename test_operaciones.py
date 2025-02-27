import pytest
from operaciones import Operaciones
from funciones_extra import FuncionesExtra

def test_sumar():
    op = Operaciones()
    assert op.sumar(2, 2) == 4
    
def test_restar():
    op = Operaciones()
    assert op.restar(10, 5) == 5
    
def test_multiplicar():
    op = FuncionesExtra()
    assert op.multiplicar(5, 2) == 10
    
def test_dividir():
    op = FuncionesExtra()
    assert op.dividir(4, 2) == 2