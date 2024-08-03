#Watthana Siamliem 653380280-0
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.CountClump import CountClump

class TestCountClump(unittest.TestCase):
    
    def setUp(self):
        # Code to set up the test environment before each test
        self.test_cases = {
            'none': None,
            'empty': [],
            'with_clumps': [1, 1, 1, 2, 2]
        }

    def tearDown(self):
        # Code to clean up after each test
        self.test_cases = None

    def test_nums_is_none(self):
        result = CountClump.count_clumps(self.test_cases['none'])
        self.assertEqual(result, 0, "Failed for nums = None")
    
    def test_nums_is_empty(self):
        result = CountClump.count_clumps(self.test_cases['empty'])
        self.assertEqual(result, 0, "Failed for nums = []")
    
    def test_nums_with_clumps(self):
        result = CountClump.count_clumps(self.test_cases['with_clumps'])
        self.assertEqual(result, 2, "Failed for nums = [1, 1, 1, 2, 2]")

if __name__ == '__main__':
    unittest.main()
