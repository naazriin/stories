import unittest
from main import *



class TestFunction(unittest.TestCase):

    def test_sum_f(self):   
        a = 5
        b = 3
        expected = 9
        actual = sum_f(a, b)
        self.assertEqual(actual, expected)

    def test_divie(self):
        a = 6
        b = 2
        expected = 2
        actual = divide(a, b)
        self.assertEqual(actual, expected)

    def test_zeros(self):
        a = 4
        b = 0
        with self.assertRaises(ZeroDivisionError):
            divide(a, b)

if __name__ == '__main__':
    unittest.main()