from dataclasses import dataclass, field
import sys, os
from typing import Tuple

from numpy import Infinity
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution
from rich.console import Console

@dataclass(order=True)
class ShortPath():
    distance: int = Infinity
    visited: bool = False
    node_from: Tuple = ()

@dataclass  
class Day15Solution(Solution):
    matrix: list = field(default_factory=list)
    path_to_end: list = field(default_factory=list)
    prio_q: list = field(default_factory=list)
    entries: dict = field(default_factory=dict)
    start: tuple = (0, 0)
    end: tuple = ()
    
    def __post_init__(self):
        self.matrix = [[int(x) for x in row] for row in self.raw_input()]
        self.width = len(self.matrix[0])
        self.length = len(self.matrix)
        if not self.end:
            self.end = (self.width - 1, self.length - 1)
        
    def solve_part1(self):
        result = self.shortest_path()
        return result

    def solve_part2(self):
        return 0
    
    def shortest_path(self):
        unvisited = []
        for y in range(self.length):
            for x in range(self.width):
                unvisited.append((x, y))
        cur_node = self.start
        self.entries = {t: ShortPath() for t in unvisited}
        self.entries[self.start].distance, self.entries[self.start].node_from = 0, self.start
        nbs = []
        while self.end not in nbs:
            i, j = cur_node
            nbs = [nb for nb  in self.get_neighbours(i, j) if not self.entries[nb].visited]
            for nb in nbs:
                d = self.entries[cur_node].distance + self.matrix[nb[1]][nb[0]]
                if d < self.entries[nb].distance:
                    self.entries[nb] = ShortPath(distance=d,
                                           node_from=cur_node)
            self.entries[cur_node].visited = True
            self.prio_q = sorted([item for item in self.entries.items() if not item[1].visited],
                               key=lambda item: item[1].distance)
            cur_node = self.prio_q[0][0]      
        self.set_path_to_end()
        
        return self.entries[self.end].distance
    
    def get_neighbours(self, i, j):
        neighbours = [(x + i, y + j) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        neighbours = [(x, y) for (x, y) in neighbours if self.check_boundary(x, y)]
        return neighbours

    def check_boundary(self, x, y):
        l = len(self.matrix)
        w = len(self.matrix[0])
        return x >= 0 and x < l and y >= 0 and y < w
    
    def set_path_to_end(self):
        width = len(self.matrix[0])
        length = len(self.matrix) 
        
        end = (width - 1, length - 1)
        cur_node = end
        while cur_node != self.start:
            self.path_to_end.append(cur_node)
            cur_node = self.entries[cur_node].node_from
        self.path_to_end.append(self.start)
        self.path_to_end = [item for item in reversed(self.path_to_end)]
    
    def to_str(self):
        return '\n'.join([self.format_line(j) for j, line in enumerate(self.matrix)])
        
    def format_line(self, j):
        result = ''
        for (i, x) in enumerate(self.matrix[j]):
            style = 'green' if (i, j) in self.path_to_end else 'red'
            result += f'[{style}]{x}[/]'
        return result
    
def main():
    console = Console()
    p0 = Day15Solution('day15/simple.input')
    result0 = p0.solve_part1()
    console.print(f'{p0.to_str()}\n')
    
    p1 = Day15Solution('day15/example.input')
    result1 = p1.solve_part1()
    console.print(f'{p1.to_str()}\n')
    
    # p2 = Day15Solution('day15/puzzle.input')
    # result2 = p2.solve_part1()
    # console.print(p2.to_str())


if __name__ == '__main__':
    main()