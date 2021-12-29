# , \d+
import unittest, sys
from day14 import Day14Solution
from rich.console import Console

class test_solve_day14(unittest.TestCase):
    def setUp(self):
        self.example = Day14Solution('day14/example.input')
        self.puzzle = Day14Solution('day14/puzzle.input')

    def test_example1(self):
        self.assertEqual(self.example.solve_part1(), 1588)

    def test_puzzle1(self):
        self.assertEqual(self.puzzle.solve_part1(), 2003)

    def test_example2(self):
        self.assertEqual(self.example.solve_part2(), 2188189693529)

    def test_puzzle2(self):
        self.assertEqual(self.puzzle.solve_part2(), 2276644000111)

def main():
    console = Console()
    try:
        s = unittest.main()
    except:
        console.print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()