# , \d+
import unittest, sys
from day10 import Day10Solution

class test_solve_day10(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = Day10Solution('day10/example.input')
        self.puzzle = Day10Solution('day10/puzzle.input')

    def test_example1(self):
        self.assertEqual(self.example.solve_part1(), 26397)

    def test_puzzle1(self):
        self.assertEqual(self.puzzle.solve_part1(), 243939)

    def test_example2(self):
        self.assertEqual(self.example.solve_part2(), 288957)

    def test_puzzle2(self):
        self.assertEqual(self.puzzle.solve_part2(), 2421222841)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()