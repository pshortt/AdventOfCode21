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
    try:
        p1 = DayNSolution('example.input').solve_part1()
        print(f'solve_part1: {p1}')
        p2 = DayNSolution('example.input').solve_part2()
        print(f'solve_part1: {p2}')
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()