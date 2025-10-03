import unittest
from lab2 import  guess_number

class TestMath (unittest.TestCase):

        def test_1(self):
            result, atts = guess_number(5, 1, 10)
            self.assertEqual(result, 5)
            self.assertEqual(atts, 5)

        def test_2(self):
            result, atts = guess_number(1, 1, 100)
            self.assertEqual(result, 1)
            self.assertEqual(atts, 1)

        def test_3(self):
            result, atts = guess_number(5, 5, 5)
            self.assertEqual(result, 5)
            self.assertEqual(atts, 1)



import unittest
from lab2 import binary_guess_number

class TestMath2 (unittest.TestCase):


    def test_11(self):
            result, attempts = binary_guess_number(5, 1, 10)
            self.assertEqual(result, 5)
            self.assertLessEqual(attempts, 4)

    def test_12(self):
            result, attempts = binary_guess_number(1, 1, 100)
            self.assertEqual(result, 1)
            self.assertLessEqual(attempts, 7)

    def test_13(self):
            result, attempts =binary_guess_number(100, 1, 100)
            self.assertEqual(result, 100)
            self.assertLessEqual(attempts, 7)


if __name__=="_main_":
    unittest.main()








