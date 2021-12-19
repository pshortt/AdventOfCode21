# , \d+
import unittest, sys
from day9 import Day9Solution

class test_solve_day9(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.example = Day9Solution('day9/example.input')
        self.puzzle = Day9Solution('day9/puzzle.input')

    def test_example1(self):
        self.assertEqual(self.example.solve_part1(), 15)

    def test_puzzle1(self):
        self.assertEqual(self.puzzle.solve_part1(), 580)

    def test_example2(self):
        self.assertEqual(self.example.solve_part2(), 1134)

    def test_puzzle2(self):
        self.assertEqual(self.puzzle.solve_part2(), 856716)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()