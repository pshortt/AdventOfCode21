import unittest
from day16 import Day16Solution

class test_solve_day16(unittest.TestCase):
    def setUp(self):
        self.example = Day16Solution(
            'day16/example.input')
        self.puzzle = Day16Solution(
            'day16/puzzle.input')

    # def test_example1(self):
        # self.assertEqual(
        #     self.example.solve_part1(), 31)

    def test_puzzle1(self):
        self.assertEqual(
            self.puzzle.solve_part1(), 943)

    # def test_example2(self):
    #     self.assertEqual(
    #         self.example.solve_part2(), -1)

    def test_puzzle2(self):
        self.assertEqual(
            self.puzzle.solve_part2(), 167737115857)

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
