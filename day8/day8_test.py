# , \d+
import unittest
from day8 import solve_part1, solve_part2

class test_solve_day8(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('day8/example.input'), 26)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('day8/puzzle.input'), 310)

    def test_example2(self):
        self.assertEqual(solve_part2('day8/example.input'), 61229)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('day8/puzzle.input'), 915941)

        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass