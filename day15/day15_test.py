import unittest
from day15 import Day15Solution

class test_solve_day15(unittest.TestCase):
    def setUp(self):
        self.example = Day15Solution(
            'day15/example.input')
        self.puzzle = Day15Solution(
            'day15/puzzle.input')

    def test_example1(self):
        self.assertEqual(
            self.example.solve_part1(), 40)

    def test_puzzle1(self):
        self.assertEqual(
            self.puzzle.solve_part1(), 613)

    def test_example2(self):
        self.assertEqual(
            self.example.solve_part2(), 315)

    def test_puzzle2(self):
        self.assertEqual(
            self.puzzle.solve_part2(), 2899)

def main():
    unittest.main()

if __name__ == '__main__':
    main()