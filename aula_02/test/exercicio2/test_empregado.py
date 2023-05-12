import unittest
from empregado import Empregado

class TestEmpregado(unittest.TestCase):

    def test_calcular_reajuste(self):
        empregado = Empregado("João", "Lucas", "analista", 5000)
        esperado = 1.05 * 5000
        self.assertEqual(
            empregado.calcular_reajuste(),
            esperado)
    
    def test_gerar_nome_completo(self):
        empregado = Empregado("João", "Lucas", "analista", 5000)
        esperado = "João Lucas"
        self.assertEqual(
            empregado.gerar_nome_completo(),
            esperado)
        
    def test_validar_cargo_analista(self):
        empregado = Empregado("João", "Lucas", "analista", 5000)
        entrada = empregado.validar_cargo()
        esperado = True
        self.assertEqual(
            entrada,
            esperado)
        
    def test_validar_cargo_presidente(self):
        empregado = Empregado("Rahul", "Couto", "presidente", 5000)
        esperado = True
        self.assertEqual(
            empregado.validar_cargo(),
            esperado)
        
    def test_validar_cargo_gerente(self):
        empregado = Empregado("Luan", "Ribeiro", "gerente", 5000)
        esperado = True
        self.assertEqual(
            empregado.validar_cargo(),
            esperado)
    
    def test_validar_cargo_diretor(self):
        empregado = Empregado("Jessica", "Celestino", "diretor", 5000)
        esperado = True
        self.assertEqual(
            empregado.validar_cargo(),
            esperado)

    def test_validar_cargo_auxiliar(self):
        empregado = Empregado("Gean", "Lucas", "auxiliar", 5000)
        esperado = True
        self.assertEqual(
            empregado.validar_cargo(),
            esperado)
    
    def test_validar_cargo_estagiario(self):
        empregado = Empregado("Raluca", "Clodovil", "estagiario", 5000)
        esperado = False
        self.assertEqual(
            empregado.validar_cargo(),
            esperado)


if __name__ == "__main__":
    unittest.main()
