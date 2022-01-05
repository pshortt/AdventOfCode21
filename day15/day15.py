from dataclasses import dataclass, field
import sys, os
from typing import Tuple

from numpy import Infinity, mat
from prio_q import PriorityQueue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

@dataclass()
class DJNode():
    distance: int = 0
    risk: int = 0
    node_from: tuple = field(default_factory=tuple)
    visited: bool = False

@dataclass  
class Day15Solution(Solution):
    matrix: list = field(default_factory=list)
    path_to_end: list = field(default_factory=list)
    start: tuple = (0, 0)
    end: tuple = ()
    prio_q: PriorityQueue = field(default_factory=PriorityQueue)
    EXPAND: int = 5

    def prepare(self, part2=False):
        self.set_matrix(
            matrix=[[int(x) for x in row] for row in self.raw_input()],
        )
        if part2:
            self.discover_all_tiles()
        self.end = (self.width - 1, self.length - 1)
        for j, row in enumerate(self.matrix):
            for i, r in enumerate(row):
                d = 0 if (i, j) == self.start else Infinity
                self.set_node(
                    loc=(i, j),
                    risk=r,
                    distance=d,)

    def solve_part1(self):
        self.prepare()
        result = self.shortest_path()
        return result

    def solve_part2(self):
        self.prepare(part2=True)
        result = self.shortest_path()
        return result

    def set_matrix(self, matrix):
        self.matrix = matrix
        self.width = len(self.matrix[0])
        self.length = len(self.matrix)

    def set_node(self, loc, distance, risk, 
                 node_from=(), visited=False):        
        i, j = loc
        self.matrix[j][i] = DJNode(
            distance=distance,
            risk=risk,
            node_from=node_from,
            visited=visited,
        )
        self.prio_q.add_task((i, j), distance)

    def shortest_path(self):
        while True:
            cur_node = self.visit()
            nbs = self.get_neighbours(cur_node)
            if self.end in nbs:
                self.handle_nb(cur_node, self.end)
                return self.matrix[self.end[1]][self.end[0]].distance
            else:
                [self.handle_nb(cur_node, nb) for nb in nbs]

    def get_neighbours(self, node):
        i, j = node
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        nbs = [(x + i, y + j) for x, y in offsets]
        nbs = [(x, y) for (x, y) in nbs if self.check_boundary(x, y)]
        return nbs

    def check_boundary(self, x, y):
        return x >= 0 and x < self.length \
            and y >= 0 and y < self.width

    def visit(self):
        i, j = self.pop_task()
        self.matrix[j][i].visited = True
        return (i, j)

    def pop_task(self):
        try:
            i, j = self.prio_q.pop_task()
        except KeyError as e:
            print('Error: finished queue before reaching end.')
        return (i, j)

    def handle_nb(self, cur_node, nb):
        i_cur, j_cur = cur_node
        i_ne, j_ne = nb
        nb = self.matrix[j_ne][i_ne]
        cur_node = self.matrix[j_cur][i_cur]
        if not nb.visited:
            d = cur_node.distance + nb.risk
            if d < nb.distance:
                self.set_node(
                    loc=(i_ne, j_ne),
                    node_from=(i_cur, j_cur),
                    risk = nb.risk,
                    distance=d,
                    )

    def discover_all_tiles(self):
        new_matrix = []
        exp = 5
        for _ in range(self.length*exp):
            new_matrix.append(['' for _ in range(self.width*exp)])
        for j, row in enumerate(self.matrix):
            for i, x in enumerate(row):
                self.format_new_matrix(i, j, new_matrix)
        self.set_matrix(new_matrix)

    def format_new_matrix(self, i, j, new_matrix):
        for y in range(self.EXPAND):
            for x in range(self.EXPAND):
                u, v = (i + x*self.width, j + y*self.length)
                new_matrix[v][u] = (self.matrix[j][i] + x + y - 1) % 9 + 1
                
def main():
    pass

if __name__ == '__main__':
    main()