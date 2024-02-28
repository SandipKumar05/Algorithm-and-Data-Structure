# first write the test case
import unittest

class TddPythonExample(unittest.TestCase):
    def test_calc_add_method(self):
        calc = calculator()
        result = calc.add(2,3)
        actual_result = 5
        self.assertEqual(actual_result, result)
    def test_value_error(self):
        calc = calculator()
        self.assertRaises(ValueError, calc.add, 'two', 'three')

class calculator:
    def add(self, x, y):
        number_type = (int,float,complex)
        if isinstance(x, number_type) and isinstance(y, number_type):
            return x+y
        else:
            raise ValueError

if __name__ == '__main__':
    unittest.main()
    