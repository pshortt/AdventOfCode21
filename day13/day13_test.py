# , \d+
import unittest, sys
from day13 import Day13Solution

class test_solve_day13(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_example1(self):
        self.example = Day13Solution('day13/example.input')
        self.assertEqual(self.example.solve_part1(), 17)

    def test_puzzle1(self):
        self.puzzle = Day13Solution('day13/puzzle.input')
        self.assertEqual(self.puzzle.solve_part1(), 671)

def main():
    try:
        unittest.main()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()