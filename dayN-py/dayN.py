from dataclasses import dataclass, field
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

@dataclass  
class DayNSolution(Solution):
    input: list = field(default_factory = list)
    
    def __post_init__(self):
        self.input = self.raw_input()
    
    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0
    
def main():
    inp = 'example.input'
    p1 = DayNSolution(inp).solve_part1()
    print(f'solve_part1: {p1}')
    p2 = DayNSolution(inp).solve_part2()
    print(f'solve_part1: {p2}')

if __name__ == '__main__':
    main()
    