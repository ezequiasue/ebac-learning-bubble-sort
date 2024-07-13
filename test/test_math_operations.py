import unittest
import sys
import os

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Agora importa a função que será testada
from tdd.math_operations import *

class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        math_addition_result = addition_operation(number1=5, number2=10)
        self.assertEqual(math_addition_result, 15)
        
        
    def test_subtraction_operation(self):
        math_subtraction_result = subtraction_operation(number1=5, number2=10)
        self.assertEqual(math_subtraction_result, -5)

if __name__ == '__main__':
    unittest.main()
