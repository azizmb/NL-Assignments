import combinations
import unittest

class TestCombinations(unittest.TestCase):

    def test_combinations(self):
        c = combinations.generate_combinations("WXYZ", 2)
        res = [
            ['W', 'X'], ['W', 'Y'], ['W', 'Z'],
            ['X', 'Y'], ['X', 'Z'],
            ['Y', 'Z']
        ]
        self.assertEqual(c, res)
        
        c = combinations.generate_combinations("WWYZ", 3)
        res = [
            ['W', 'W', 'Y'], ['W', 'W', 'Z'],
            ['W', 'Y', 'Z'], ['W', 'Y', 'Z'],
        ]
        self.assertEqual(c, res)

    def test_invalid_n(self):
        c = combinations.generate_combinations("WWYZ", 5)
        self.assertEqual(len(c), 0)

if __name__ == '__main__':
    unittest.main()