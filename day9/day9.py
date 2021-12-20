from typing import Tuple
import numpy as np
from dataclasses import dataclass, field
import sys, os
sys.path.append(os.getcwd())
from solution import Solution

@dataclass  
class Day9Solution(Solution):
    matrix: list = field(default_factory = list)
    
    def __post_init__(self):
        self.matrix = self.raw_input()
    
    def solve_part1(self):
        return np.array([int(self.matrix[x][y]) + 1 for x, y in self.low_points()]).sum()

    def solve_part2(self):
        basins = self.get_basins()
        return np.array(sorted([b.size(self.matrix) for b in basins])[-3:]).prod()

    def low_points(self):
        result = []
        for (i, line) in enumerate(self.matrix):
            for (j, _) in enumerate([int(c) for c in line]):
                if self.is_low_point(i, j): result.append((i, j))
        return result

    def is_low_point(self, i, j):
        neighbours = self.get_neighbours(i, j)
        condition = lambda t: self.matrix[t[2]][t[3]] < self.matrix[t[0]][t[1]]
        return len(neighbours) == len(self.get_neighbours_with(i, j, condition))

    def get_neighbours(self, i, j):
        neighbours = [(x + i, y + j) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        neighbours = [(x, y) for (x, y) in neighbours if self.check_boundary(x, y)]
        return neighbours

    def check_boundary(self, x, y):
        l = len(self.matrix)
        w = len(self.matrix[0])
        return x >= 0 and x < l and y >= 0 and y < w

    def get_neighbours_with(self, i, j, condition):
        neighbours = self.get_neighbours(i, j)
        return [(x, y) for (x, y) in neighbours if condition((x, y, i, j))]

    def get_basins(self):
        basins = []
        for i,j  in self.low_points():
            if not any([b.contains(i, j) for b in basins]):
                s = self.search_for_basin(i, j)
                b = basin([p for p in s]) 
                if b.size(self.matrix) > 0: basins.append(b)         
        return basins

    def search_for_basin(self, i, j):
        result = set()
        if not self.basin_condition((i, j)):
            return result
        else:
            self._recursive_search_for_basin(i, j, result)
            return result

    def _recursive_search_for_basin(self, i, j, result):
        result.add((i,j))
        condition = lambda t : self.basin_condition(t)
        neighbours = [nb for nb in self.get_neighbours_with(i, j, condition) if nb not in result]      
        for x, y in neighbours:
            self._recursive_search_for_basin(x, y, result)

    def basin_condition(self, t):
        return self.matrix[t[0]][t[1]] != '9'

@dataclass
class basin:
    eles: list[Tuple] = field(default_factory=list)
    
    def append(self, t) -> None:
        self.eles.append(t)
        
    def contains(self, i, j) -> bool:
        return (i, j) in self.eles
    
    def size(self, matrix) -> int:
        return len(self.eles) 