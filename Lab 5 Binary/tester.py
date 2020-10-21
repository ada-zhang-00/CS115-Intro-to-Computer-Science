'''
CS 115 - Lab 5 Public Test Script
'''

import unittest
import Lab5

# Place this file in the same directory as Lab5.py when you run it!

class Test(unittest.TestCase):

    def test_DecToBin(self):
        self.assertEqual(Lab5.decimalToBinary(1), [1])
        self.assertEqual(Lab5.decimalToBinary(257), [1, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_BinToDec(self):
        self.assertEqual(Lab5.binaryToDecimal([1, 0, 1, 1, 1, 0, 0, 1, 1]), 413)
        self.assertEqual(Lab5.binaryToDecimal([0, 1, 0, 1]), 10)

    def test_incBin(self):
        self.assertEqual(Lab5.incrementBinary([1, 1, 1]), [0, 0, 0, 1])
        self.assertEqual(Lab5.incrementBinary([1, 1, 0, 0, 1]), [0, 0, 1, 0, 1])

    def test_addBin(self):
        self.assertEqual(Lab5.addBinary([0, 0, 1], [1, 0, 1, 1]), [1, 0, 0, 0, 1])
        self.assertEqual(Lab5.addBinary([1, 0, 1, 1], [0, 0, 1]), [1, 0, 0, 0, 1])
        self.assertEqual(Lab5.addBinary([1, 0, 0, 0, 1], [1, 0, 1, 1]), [0, 1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()
