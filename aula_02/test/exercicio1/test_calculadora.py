import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_somar_1(self):
       entrada = Calculadora().somar(5, 7)
       esperado = 12

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_somar_2(self):
       entrada = Calculadora().somar(-3, 3)
       esperado = 0

       self.assertEqual(
            entrada, 
            esperado)
    
    def test_somar_3(self):
       entrada = Calculadora().somar(0, 0)
       esperado = 0

       self.assertEqual(
            entrada, 
            esperado)
    
    def test_subtrair_1(self):
       entrada = Calculadora().subtrair(10, 5)
       esperado = 5

       self.assertEqual(
            entrada, 
            esperado)
    
    def test_subtrair_2(self):
       entrada = Calculadora().subtrair(-3, 3)
       esperado = -6

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_subtrair_3(self):
       entrada = Calculadora().subtrair(0, 0)
       esperado = 0

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_multiplicar_1(self):
       entrada = Calculadora().multiplicar(3, 7)
       esperado = 21

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_multiplicar_2(self):
       entrada = Calculadora().multiplicar(-3, 3)
       esperado = -9

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_multiplicar_3(self):
       entrada = Calculadora().multiplicar(0, 0)
       esperado = 0

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_dividir_1(self):
       entrada = Calculadora().dividir(10, 2)
       esperado = 5

       self.assertEqual(
            entrada, 
            esperado)
    
    def test_dividir_2(self):
       entrada = Calculadora().dividir(-6, 3)
       esperado = -2

       self.assertEqual(
            entrada, 
            esperado)
       
    def test_dividir_3(self):
       entrada = Calculadora().dividir(10, 5)
       esperado = 2

       self.assertEqual(
            entrada, 
            esperado)