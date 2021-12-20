from dataclasses import dataclass
from abc import abstractmethod

@dataclass
class Solution():
    '''Template for a solution for an Advent of Code puzzle'''
    filename: str
   
    @abstractmethod
    def solve_part1(self) -> int:
        '''
        Implement solution to part 1
        '''
        return

    @abstractmethod
    def solve_part2(self) -> int:
        '''
        Implement solution to part 2
        '''
        return

    # Class methods
    def raw_input(self):
       with open(self.filename) as f:
            return [l.strip() for l in f.readlines()]    