# , \d+
import unittest, sys
from day15 import Day15Solution

class test_solve_day15(unittest.TestCase):
    def setUp(self):
        self.example = Day15Solution('day15/example.input')
        self.puzzle = Day15Solution('day15/puzzle.input')

    def test_example1(self):
        self.assertEqual(self.example.solve_part1(), 40)

    # def test_puzzle1(self):
    #     self.assertEqual(self.puzzle.solve_part1(), -1)

    # def test_example2(self):
    #     self.assertEqual(self.example.solve_part2(), -1)

    # def test_puzzle2(self):
    #     self.assertEqual(self.puzzle.solve_part2(), -1)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()