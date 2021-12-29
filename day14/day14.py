from dataclasses import dataclass, field
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution
@dataclass
class RuleMapNode():
    inp: str
    left_child: str = field(default_factory=str)
    right_child: str = field(default_factory=str)
    count: int = 0
    
    def __post_init__(self):
        self.left_child = self.inp[0][0] + self.inp[1]
        self.right_child = self.inp[1] + self.inp[0][1]
    
    def copy(self):
        return RuleMapNode(inp=self.inp,
                           left_child=self.left_child,
                           right_child=self.right_child,
                           count=self.count)

@dataclass  
class Day14Solution(Solution):
    input: list = field(default_factory = list)
    template: str = field(default_factory = str)
    rules: dict = field(default_factory = dict)
    leading_c: str = field(default_factory = str)
    
    def __post_init__(self):
        self.input = self.raw_input()
        self.template = self.input[0]
        self.leading_c = self.template[0]
        self.rules = {s.split(' -> ')[0] : s.split(' -> ')[1] for s in self.input[2:]}
        for s in self.input[2:]:
            s = s.split(' -> ')
            self.rules[s[0]] = RuleMapNode(s)
        for i, c in enumerate(self.template[:-1]):
            self.rules[c + self.template[i + 1]].count += 1
    
    def solve_part1(self):
        for _ in range(10):  
            self.step()  
        result = self.count_letters()
        return result

    def solve_part2(self):
        for _ in range(40):
            self.step()        
        result = self.count_letters()
        return result
    
    def step(self):
        new_rules = {key: rule.copy() for key, rule in self.rules.items()}
        for key, rule in self.rules.items():
            new_rules[rule.left_child].count += rule.count
            new_rules[rule.right_child].count += rule.count
            new_rules[key].count -= rule.count 
        self.rules = new_rules
        
    def count_letters(self):
        count = {c : 0 for c in  self.unique_letters()}
        count[self.leading_c] += 1
        for key, rule in self.rules.items():
            count[key[1]] += rule.count
        count = [x for _, x in count.items()]
        return max(count) - min(count)
        
    def unique_letters(self):
        unique_letters = set()
        for key, _ in self.rules:
            for c in key:
                unique_letters.add(c)
        return unique_letters
        
def main():
    try:
        p1 = Day14Solution('example.input').solve_part1()
        print(f'solve_part1: {p1}')
        p2 = Day14Solution('example.input').solve_part2()
        print(f'solve_part1: {p2}')
    except:
        print(f'Error: {sys.exc_info()[0]} : {sys.exc_info()[1]}')

if __name__ == '__main__':
    main()