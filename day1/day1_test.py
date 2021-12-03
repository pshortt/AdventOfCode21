import unittest
from day1 import solve_part1, solve_part2


class TestSolveCountIncrease(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example01(self):
        self.assertEqual(solve_part1('example.input'), 7)

    def test_puzzle01(self):
        self.assertEqual(solve_part1('puzzle.input'), 1564)

    def test_example02(self):
        self.assertEqual(solve_part2('example.input'), 5)

    def test_puzzle02(self):
        self.assertEqual(solve_part2('puzzle.input'), 1611)
        
if __name__ == '__main__':
    unittest.main()