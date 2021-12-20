from dataclasses import dataclass, field
import sys, os
sys.path.append(os.getcwd())
from solution import Solution

@dataclass  
class DayNSolution(Solution):
    input: list = field(default_factory = list)
    
    def __post_init__(self):
        self.input = self.input()
    
    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0