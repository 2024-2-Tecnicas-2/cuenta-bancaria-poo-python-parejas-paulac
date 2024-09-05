import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalcular(unittest.TestCase):
    def test_ingresar(self):
        self.cuenta.ingresar(2000)
        self.assertEqual(self.cuenta.getSaldo(), 8000.0)
        
    
    def test_retirar(self):
        self.cuenta.retirar(2000)
        self.assertEqual(self.cuenta.getSaldo(), 6000.0)
