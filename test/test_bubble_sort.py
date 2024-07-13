import unittest
import sys
import os

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Agora importa a função que será testada
from tdd.bubble_sort import *

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted_list = [66, 11, 4,8, 1, 70]
        expected_list = [1, 4, 8, 11, 66, 70]
        
        print('Before', unsorted_list)

        unsorted_list = bubble_sort(unsorted_list)
        
        print('After', unsorted_list)
        
        self.assertEqual(unsorted_list, expected_list) 
        
if __name__ == '__main__':
    unittest.main()
