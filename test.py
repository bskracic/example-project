import unittest

import math_utils as mu

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mu.add(2, 3), 5)
        self.assertEqual(mu.add(-1, 1), 0)
        self.assertEqual(mu.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()