import unittest
from dayN import DayNSolution

class test_solve_dayN(unittest.TestCase):
    def setUp(self):
        self.example = DayNSolution(
            'dayN/example.input')
        self.puzzle = DayNSolution(
            'dayN/puzzle.input')

    def test_example1(self):
        self.assertEqual(
            self.example.solve_part1(), -1)

    def test_puzzle1(self):
        self.assertEqual(
            self.puzzle.solve_part1(), -1)

    def test_example2(self):
        self.assertEqual(
            self.example.solve_part2(), -1)

    def test_puzzle2(self):
        self.assertEqual(
            self.puzzle.solve_part2(), -1)

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()