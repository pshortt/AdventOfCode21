# , \d+
import unittest
from day7 import solve_part1, solve_part2

class test_solve_day7(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('day7/example.input'), 37)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('day7/puzzle.input'), 355521)

    def test_example2(self):
        self.assertEqual(solve_part2('day7/example.input'), 168)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('day7/puzzle.input'), 100148777)

        
if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass