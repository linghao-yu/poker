import unittest
from poker import compare_unit

class PokerTestCase(unittest.TestCase):

    def testcase1(self):
        s = "2H 3D 5S 9C KD"
        q = "2C 3H 4S 8C AH"
        result1 = compare_unit(s , q)
        self.assertEqual(result1, 'White wins-high card:Ace')

    def testcase2(self):
        s = "2H 3D 5S 9C KD"
        q = "2C 3H 4S 8C KH"
        result2 = compare_unit(s , q)
        self.assertEqual(result2, 'Black wins-high card:9')

    def testcase3(self):
        s = "2H 4S 4C 2D 4H"
        q = "2S 8S AS QS 3S"
        result3 = compare_unit(s , q)
        self.assertEqual(result3, 'Black wins-Full House')

    def testcase4(self):
        s = "2H 3D 5S 9C KD"
        q = "2D 3H 5C 9S KH"
        result4 = compare_unit(s , q)
        self.assertEqual(result4, 'Tie')

if __name__ == '__main__':
    unittest.main()