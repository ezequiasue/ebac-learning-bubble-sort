import unittest
import sys
import os

# Adiciona o diretório do projeto ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from tdd.binary_search import *

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 8
        
        result  = binary_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 5)
        
        
if __name__ == '__main__':
    unittest.main()
