from dataclasses import dataclass, field
import sys, os
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

@dataclass  
class Day13Solution(Solution):
    input: list = field(default_factory = list)
    dots: list = field(default_factory = list)
    folds: list = field(default_factory = list)
    paper: list = field(default_factory = list)
    
    def __post_init__(self):
        self.input = self.raw_input()
        i = self.input.index('')
        self.dots = [(int(s.split(',')[0]), int(s.split(',')[1])) for s in self.input[:i]]
        self.folds = [(s.split('=')[0][-1], int(s.split('=')[1])) for s in self.input[i + 1:]]
        width = max([d[0] for d in self.dots]) + 1
        length = max([d[1] for d in self.dots]) + 1
        self.paper = [['#' if (i, j) in self.dots else '.' for i in range(width)] for j in range(length)]
    
    def solve_part1(self):
        self.execute_fold(0)
        result = np.array([[int(c == '#') for c in row] for row in self.paper]).sum()
        return result

    def solve_part2(self):
        for i, _ in enumerate(self.folds):
            self.execute_fold(i)
        print(f'\n{self.paper_to_str()}\n')
        return 0
    
    def paper_to_str(self):
        return '\n'.join([''.join(row) for row in self.paper])
    
    def execute_fold(self, i):
        fold = self.folds[i]
        match fold[0]:
            case 'x':
                self.foldx(fold[1])
            case 'y':
                self.foldy(fold[1])
    
    def foldx(self, loc):
        left = [row[:loc] for row in self.paper]
        right = [reversed(row[loc + 1:]) for row in self.paper]
        self.fold(left, right)
    
    def foldy(self, loc):
        top = self.paper[:loc]
        bottom = reversed(self.paper[loc + 1:])
        self.fold(top, bottom)
    
    def fold(self, side1, side2):
        iter = zip(side1, side2)
        result = [[self.eval_loc(c1, c2) for c1, c2 in zip(row1, row2)] for row1, row2 in iter]
        self.paper = result
        
    def eval_loc(self, p1, p2):
        return '.' if p1 == '.' and p2 == '.' else '#'
    
def main():
    try:        
        Day13Solution('example.input').solve_part2()      
        Day13Solution('puzzle.input').solve_part2()
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()