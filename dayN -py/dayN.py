from dataclasses import dataclass
import sys, os
sys.path.append(os.getcwd())
from solution import Solution

@dataclass  
class DayNSolution(Solution):
    '''field to represent input'''
    
    def __post_init__(self):
        '''set input field with self.input()'''
    
    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0