""" Importing Unit Test Module"""
import unittest

class Calculator:
    """Defining Class Calculator"""
    def add(self, x_1, y_1):
        """
        Add two numbers.
        Args:
            X (int): The first number.
            Y (int): The second number.
        Returns:
            int: The sum of X and Y.
        """
        return x_1 + y_1

    def subtract(self, X, Y):
        """
        Subtract two numbers.
        Args:
            X (int): The first number.
            Y (int): The second number.
        Returns:
            int: The result of subtracting Y from X.
        """
        return X - Y

    def multiply(self, X, Y):
        """
        Multiply two numbers.
        Args:
            X (int): The first number.
            Y (int): The second number.
        Returns:
            int: The product of X and Y.
        """
        return X * Y

    def divide(self, X, Y):
        """
        Divide two numbers.
        Args:
            X (float): The numerator.
            Y (float): The denominator.
        Returns:
            float: The result of dividing X bY Y.
        Raises:
            ValueError: If the denominator (Y) is 0.
        """
        if Y == 0:
            raise ValueError("Division by zero is not allowed")
        return X / Y

class CalculatorTest(unittest.TestCase):
    """Defining Tests"""
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """
        Test addition method.
        """
        self.assertEqual(11, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        """
        Test subtraction method.
        """
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        """
        Test multiplication method.
        """
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        """
        Test division method.
        """
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()
