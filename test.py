"""Tests"""  

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Tests de transformació de strings"""  

    def test_is_upper(self):
        """hauria de retornar HELLO (majúscules)."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_is_lower(self):
        """hauria de retornar hello (minúscules)."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_is_capitalize(self):
        """hauria de retornar Hello (normal)."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")


if __name__ == "__main__":
    unittest.main()
