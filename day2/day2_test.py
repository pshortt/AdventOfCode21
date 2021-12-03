import unittest
from day2 import solve_part1, solve_part2

class TestSolveDay2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.assertEqual(solve_part1('example.input'), 150)

    def test_puzzle1(self):
        self.assertEqual(solve_part1('puzzle.input'), 2117664)

    def test_example2(self):
        self.assertEqual(solve_part2('example.input'), 900)

    def test_puzzle2(self):
        self.assertEqual(solve_part2('puzzle.input'), 2073416724)

        
if __name__ == '__main__':
    unittest.main()