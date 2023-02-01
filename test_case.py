import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator()

    def test_addition(self):
        result = self.Calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result = self.Calculator.subtract(4, 2)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.Calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.Calculator.divide(6, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()