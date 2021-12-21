# , \d+
import unittest
import sys
from day11 import Day11Solution

class test_solve_day11(unittest.TestCase):
    def setUp(self):
        self.example = Day11Solution('day11/example.input')
        self.puzzle = Day11Solution('day11/puzzle.input')

    def test_example1(self):
        self.assertEqual(self.example.solve_part1(), 1656)

    def test_puzzle1(self):
        self.assertEqual(self.puzzle.solve_part1(), 1732)

    def test_example2(self):
        self.assertEqual(self.example.solve_part2(), 195)

    def test_puzzle2(self):
        self.assertEqual(self.puzzle.solve_part2(), 290)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()
    