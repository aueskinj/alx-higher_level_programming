#!/usr/bin/python3
import unittest
from random import choice

roman_to_int = __import__('12-roman_to_int').roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_basic_values(self):
        """Test standard Roman numeral conversions."""
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("L"), 50)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("M"), 1000)

    def test_multiple_numerals(self):
        """Test numbers composed of multiple numerals."""
        self.assertEqual(roman_to_int("II"), 2)
        self.assertEqual(roman_to_int("VII"), 7)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("LXXXVII"), 87)
        self.assertEqual(roman_to_int("DCCVII"), 707)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)  # Largest valid Roman numeral

    def test_subtraction_cases(self):
        """Test cases where subtraction rule applies."""
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XL"), 40)
        self.assertEqual(roman_to_int("XC"), 90)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("CM"), 900)

    def test_mixed_cases(self):
        """Test various valid Roman numerals."""
        self.assertEqual(roman_to_int("XIV"), 14)
        self.assertEqual(roman_to_int("XCIV"), 94)
        self.assertEqual(roman_to_int("CCCXC"), 390)
        self.assertEqual(roman_to_int("CDXLIV"), 444)
        self.assertEqual(roman_to_int("DCCCXC"), 890)

    def test_invalid_inputs(self):
        """Test invalid inputs such as non-strings and incorrect numerals."""
        self.assertEqual(roman_to_int(""), 0)  # Empty string
        self.assertEqual(roman_to_int(None), 0)  # NoneType
        self.assertEqual(roman_to_int(123), 0)  # Integer
        self.assertEqual(roman_to_int(["X", "V"]), 0)  # List
        self.assertEqual(roman_to_int("A"), 0)  # Invalid character
        self.assertEqual(roman_to_int("IIII"), 0)  # Invalid repeated numeral
        self.assertEqual(roman_to_int("VX"), 0)  # Invalid ordering
        self.assertEqual(roman_to_int("IC"), 0)  # Invalid subtraction rule

    def test_randomized_valid_numerals(self):
        """Test randomized valid Roman numeral sequences."""
        valid_romans = ["I", "V", "X", "L", "C", "D", "M"]
        random_roman = "".join(choice(valid_romans) for _ in range(5))
        result = roman_to_int(random_roman)
        self.assertIsInstance(result, int)  # Ensuring output is an integer

if __name__ == "__main__":
    unittest.main()

