import unittest
from day3 import solve_part1, solve_part2

class TestSolveDay3(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('day3/example.input'), 198)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('day3/puzzle.input'), 3958484)

    def test_example2(self):
        self.assertEqual(solve_part2('day3/example.input'), 230)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('day3/puzzle.input'), 1613181)

        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass