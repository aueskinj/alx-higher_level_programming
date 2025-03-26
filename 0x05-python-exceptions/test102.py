#!/usr/bin/python3
import unittest

from magic_calculation import magic_calculation  # Import the function if it's in another file

class TestMagicCalculation(unittest.TestCase):
    def test_normal_cases(self):
        self.assertAlmostEqual(magic_calculation(2, 3), (2 ** 3) / 1 + (2 ** 3) / 2)
        self.assertAlmostEqual(magic_calculation(3, 2), (3 ** 2) / 1 + (3 ** 2) / 2)

    def test_exception_case(self):
        self.assertEqual(magic_calculation(0, 3), 3 + 0)  # Exception should trigger

    def test_edge_cases(self):
        self.assertAlmostEqual(magic_calculation(1, 1), (1 ** 1) / 1 + (1 ** 1) / 2)
        self.assertEqual(magic_calculation(-1, 2), 2 + (-1))  # Exception should trigger

    def test_large_values(self):
        self.assertAlmostEqual(magic_calculation(10, 2), (10 ** 2) / 1 + (10 ** 2) / 2)

if __name__ == '__main__':
    unittest.main()

