"""Tests for transform module."""  

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """String transformation tests."""  

    def test_is_upper(self):
        """to_upper_case should return HELLO."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_is_lower(self):
        """To_lower_case should return hello."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_is_capitalize(self):
        """To_capitalize should return Hello."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")


if __name__ == "__main__":
    unittest.main()
