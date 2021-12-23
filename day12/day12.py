from dataclasses import dataclass, field
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

@dataclass  
class Day12Solution(Solution):
    cavern: dict = field(default_factory = dict)
    result: list = field(default_factory= list)
    part1score: int = 0
    part1: bool = True
    
    def __post_init__(self):
        inp = [line.split('-') for line in self.raw_input()]
        for home, dest in inp:
            self.cavern.setdefault(home, set())
            self.cavern.setdefault(dest, set())
            self.cavern[home].add(dest) 
            self.cavern[dest].add(home)
        self.depth_first_search()
    
    def solve_part1(self):
        return len(self.result)
    
    def solve_part2(self):
        return len(self.result)

    def depth_first_search(self, path_in=['start']) -> None:
        if path_in[-1] == 'end':
            self.result.append(path_in)
            return
        children = self.get_children(path_in)
        for child in children:
            next_path = [e for e in path_in]
            next_path.append(child)
            self.depth_first_search(next_path)
            
    def get_children(self, path_in):
        children = self.cavern[path_in[-1]]
        if self.part1 or self.small_cave_visit_check(path_in):
           result = [c for c in children if self.part1_condition(path_in, c)]
        else:
           result = [c for c in children if self.part2_condition(path_in, c)]
        return result
    
    def part1_condition(self, path_in, child):
        return not (child in path_in and child.islower())
    
    def part2_condition(self, path_in, child):
        return child != 'start' and not (path_in.count(child) > 1 and child.islower())
    
    def small_cave_visit_check(self, path_in):
        '''
        Returns true if we've viseted any small cave twice \n
        self.small_cave_visit(['start', 'a', 'B', 'a']) -> True \n
        self.small_cave_visit(['start', 'a', 'B', 'a']) -> True \n
        self.small_cave_visit(['start', 'a', 'B', 'c']) -> False \n
        self.small_cave_visit(['start', 'a', 'a', 'c', 'c']) -> Error
        '''
        cond = lambda e, p: e.islower() and p.count(e) > 1 and e != 'start'
        small_cave_count = {e : path_in.count(e) for e in set(path_in) if cond(e, path_in)}
        match len(small_cave_count):
            case 0:
                return False
            case 1:
                return True
        raise NameError('Too many small cave vists')
    
def main():
    try:
        p1 = Day12Solution('day12/example.input').solve_part1()
        print(f'solve_part1: {p1}')
        # p2 = Day12Solution('example.input').solve_part2()
        # print(f'solve_part1: {p2}')
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()   