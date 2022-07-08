import unittest.mock
import unittest

class test_random(unittest.TestCase):
    def test_assertTrue(self):
        self.assertEqual("Truman", "Truman")
    def test_assertFalse(self):
        self.assertEqual("Truman", "Mitch")

