import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_1(self):
        entrada = fizzbuzz(n=1)
        esperado = 1

        self.assertEqual(
            entrada, 
            esperado)

    def test_fizzbuzz_2(self):
        entrada = fizzbuzz(n=2)
        esperado = 2

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_3(self):
        entrada = fizzbuzz(n=3)
        esperado = 'fizz'

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_5(self):
        entrada = fizzbuzz(n=5)
        esperado = 'buzz'

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_6(self):
        entrada = fizzbuzz(n=6)
        esperado = 'fizz'

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_10(self):
        entrada = fizzbuzz(n=10)
        esperado = 'buzz'

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_15(self):
        entrada = fizzbuzz(n=10)
        esperado = 'fizzbuzz'

        self.assertEqual(
            entrada, 
            esperado)
        
    def test_fizzbuzz_30(self):
        entrada = fizzbuzz(n=30)
        esperado = 'fizzbuzz'

        self.assertEqual(
            entrada,
            esperado)
        
    def test_fizzbuzz_string(self):
        entrada = fizzbuzz(n='a')
        esperado = 'a'

        self.assertEqual(
            entrada,
            esperado)