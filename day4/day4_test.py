import unittest
from day4 import solve_part1, solve_part2

class TestSolveDay4(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('day4/example.input'), 4512)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('day4/puzzle.input'), 65325)

    def test_example2(self):
        self.assertEqual(solve_part2('day4/example.input'), 1924)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('day4/puzzle.input'), 4624)

        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass