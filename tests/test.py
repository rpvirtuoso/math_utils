import unittest
from app.math_utils import factorial, gcd, is_prime


class TestMathUtils(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))


if __name__ == '__main__':
    unittest.main()
