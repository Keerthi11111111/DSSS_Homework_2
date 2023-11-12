import unittest
import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        result = generate_random_integer(1, 10)
        self.assertTrue(1 <= result <= 10, "Generated integer is not within the specified range.")

    def test_generate_random_operator(self):
        result = generate_random_operator()
        self.assertIn(result, ['+', '-', '*'], "Generated operator is not one of the expected values.")

    def test_calculate_result(self):
        result = calculate_result(7, 6, '+')
        self.assertEqual(result, ('7 + 6', 13), "Calculation result is incorrect for addition.")

        result = calculate_result(7, 6, '-')
        self.assertEqual(result, ('7 - 6', 1), "Calculation result is incorrect for subtraction.")

        result = calculate_result(7, 6, '*')
        self.assertEqual(result, ('7 * 6', 42), "Calculation result is incorrect for multiplication.")

if __name__ == '__main__':
    unittest.main()
