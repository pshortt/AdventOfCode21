from dataclasses import dataclass, field
import sys, os
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

def empty_array() -> np.array:
    return np.array([])

@dataclass  
class Day11Solution(Solution):
    matrix: np.array = field(default_factory = empty_array)
    flashes: int = 0
    
    def __post_init__(self):
        self.matrix = np.array([[int(c) for c in row] for row in self.raw_input()])
    
    def solve_part1(self):
        for _ in range(100):
            self.step_energy_level()
        return self.flashes

    def solve_part2(self):
        inc = 0
        while not self.all_flashes():
            self.step_energy_level()
            inc += 1
        return inc
    
    def step_energy_level(self) -> None:
        self.increment()
        while self.any_flashes():
            self.eval_flashes()        
    
    def increment(self, coords=[]) -> None:
        if coords:
            f = lambda i, j, x, cs: int(x != 0 and x!= 10 and (i, j) in cs)
            mat_enum = enumerate(self.matrix)
            inc = np.array([[f(i, j, x, coords) for j, x in enumerate(row)] for i, row in mat_enum])
        else:
            inc = np.ones_like(self.matrix)
        self.matrix = np.array([self.matrix, inc]).sum(0)
    
    def any_flashes(self) -> bool:
        return 10 in self.matrix
    
    def all_flashes(self) -> bool:
        return all([all([x == 0 for x in row]) for row in self.matrix])
    
    def eval_flashes(self) -> None:
        ten_reset_mask = np.array([[-10*int(x == 10) for x in row] for row in self.matrix])
        self.flashes += int(ten_reset_mask.sum() / -10)
        for i, row in enumerate(self.matrix):
            for j, x in enumerate(row):
                if x == 10:
                    self.increment(self.get_neighbours(i, j))            
        self.matrix = np.array([self.matrix, ten_reset_mask]).sum(0)
        
    def get_neighbours(self, i, j) -> list:
        neighbour_inx = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                         (1, 1), (1, -1), (-1, 1), (-1, -1)]
        neighbours = [(x + i, y + j) for x, y in neighbour_inx]
        neighbours = [(x, y) for (x, y) in neighbours if self.check_boundary(x, y)]
        return neighbours

    def check_boundary(self, x, y) -> bool:
        l = self.matrix.shape[0]
        w = self.matrix.shape[1]
        return x >= 0 and x < l and y >= 0 and y < w
    
    def coords(self) -> list:
        return [[(i, j) for (j, _) in enumerate(row)] for (i, row) in enumerate(self.matrix)]