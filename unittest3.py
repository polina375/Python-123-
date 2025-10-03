import unittest
from lab3 import gen_bin_tree

class TestGenBinTree(unittest.TestCase):


    def test_0(self):

        result = gen_bin_tree(0, 10)
        self.assertIsNone(result)


    def test_1(self):

        result = gen_bin_tree(-1, 10)
        self.assertIsNone(result)


    def test1(self):

        result = gen_bin_tree(1, 18)

        self.assertIsInstance(result, dict)
        self.assertEqual(result['value'], 18)
        self.assertIsNone(result['left'])
        self.assertIsNone(result['right'])


    def test2(self):

        result = gen_bin_tree(2, 18)

        self.assertEqual(result['value'], 18)

        self.assertEqual(result['left']['value'], 30)
        self.assertIsNone(result['left']['left'])
        self.assertIsNone(result['left']['right'])

        self.assertEqual(result['right']['value'], 52)
        self.assertIsNone(result['right']['left'])
        self.assertIsNone(result['right']['right'])

if __name__ == '__main__':

    unittest.main()