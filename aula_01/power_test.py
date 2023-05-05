import unittest
from math_samples import MathSamples

class PowerTest(unittest.TestCase):

    def test_power01(self):
        self.assertEqual(
            MathSamples.power(0, 0),
            1)

    def test_power02(self):
        self.assertEqual(
            MathSamples.power(2, 0),
            1)

    def test_power03(self):
        self.assertEqual(
            MathSamples.power(2, 3),
            8)

    def test_power04(self):
        self.assertEqual(
            MathSamples.power(3, 3),
            27)

    def test_power05(self):
        self.assertEqual(
            MathSamples.power(10, 2),
            100)

if __name__ == '__main__':
    unittest.main()