import unittest
from day6 import solve_part1, solve_part2

class test_solve_day6(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('day6/example.input'), 5934)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('day6/puzzle.input'), 374994)

    def test_example2(self):
        self.assertEqual(solve_part2('day6/example.input'), 26984457539)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('day6/puzzle.input'), 1686252324092)

        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass