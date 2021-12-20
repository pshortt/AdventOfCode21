from dataclasses import dataclass
from solution import Solution
from numpy import array
from day9 import day9

@dataclass
class SolutionTest(Solution):
    def solve_part1(self) -> int:
        '''
        Return sum of first line
        '''
        input = self.raw_input()[0]
        return array([int(c) for c in input]).sum()
    
    def solve_part2(self) -> int:
        '''
        Return product of first line
        '''
        input = self.raw_input()[0]
        return array([int(c) for c in input]).prod()
    
if __name__ == '__main__':
    day9