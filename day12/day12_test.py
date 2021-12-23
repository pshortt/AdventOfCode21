# , \d+
import unittest, sys
from day12 import Day12Solution

class test_solve_day12(unittest.TestCase):
    def setUp(self):
        pass

    def test_example1(self):
        self.example1 = Day12Solution('day12/example.input')
        self.assertEqual(self.example1.solve_part1(), 10)

    def test_puzzle1(self):
        self.puzzle1 = Day12Solution('day12/puzzle.input')
        self.assertEqual(self.puzzle1.solve_part1(), 3450)

    def test_example2(self):
        self.example2 = Day12Solution(filename='day12/example.input', part1=False)
        self.assertEqual(self.example2.solve_part2(), 36)

    def test_puzzle2(self):
        self.puzzle2 = Day12Solution(filename='day12/puzzle.input', part1=False)
        self.assertEqual(self.puzzle2.solve_part2(), 96528)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()