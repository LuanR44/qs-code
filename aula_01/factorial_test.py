import unittest
from math_samples import MathSamples

class FactorialTest(unittest.TestCase):

    def test_factorial01(self):
        self.assertEqual(
            MathSamples.factorial(0),
            1)

    def test_factorial02(self):
        self.assertEqual(
            MathSamples.factorial(1),
            1)

    def test_factorial03(self):
        self.assertEqual(
            MathSamples.factorial(2),
            2)

    def test_factorial04(self):
        self.assertEqual(
            MathSamples.factorial(3),
            6)

    def test_factorial05(self):
        self.assertEqual(
            MathSamples.factorial(4),
            24)

    def test_factorial06(self):
        self.assertEqual(
            MathSamples.factorial(5),
            120)

    def test_factorial07(self):
        self.assertEqual(
            MathSamples.factorial(6),
            720)

if __name__ == '__main__':
    unittest.main()
