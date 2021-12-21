from dataclasses import dataclass, field
import sys, os
sys.path.append(os.getcwd())
from numpy import array
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import Solution

def opening_parentheses():
    return ['(', '[', '{', '<']

def closing_parentheses():
    return [')', ']', '}', '>']

def scores():
    return [3, 57, 1197, 25137]

def ac_char_scores():
    return [1, 2, 3, 4]

@dataclass
class Status():
    line: str
    is_valid: bool = True
    error_msg: str = ''
    score: int = 0
    autocomplete: str = ''
    autocomplete_score: int = 0

@dataclass
class Lang():
    opening_parentheses: list = field(default_factory=opening_parentheses)
    closing_parentheses: list = field(default_factory=closing_parentheses)
    scores: list = field(default_factory=scores)
    ac_char_scores: list = field(default_factory=ac_char_scores)
    
    def check_line(self, line) -> Status:
        '''
        Check for syntax errors within the context of a single line of code
        '''
        openers = [] # stack to contain opening parenthesis chars we find
        for c in line:
            if self.is_char_opener(c):
                openers.append(c)
            elif self.is_char_closer(c):
                if len(openers) == 0:
                    return Status(line, is_valid=False, 
                                  error_msg=self.error_msg(c), 
                                  score=self.score(c))
                elif not self.is_pair(openers[-1], c):
                    return Status(line, is_valid=False, 
                                  error_msg=self.error_msg(c), 
                                  score=self.score(c))
                else:
                    openers.pop()
        ac = self.autocomplete(openers)
        return Status(line, autocomplete=ac, autocomplete_score=self.autocomplete_score(ac))
    
    def is_char_opener(self, character) -> bool:
        return character in self.opening_parentheses
    
    def is_char_closer(self, character) -> bool:
        return character in self.closing_parentheses
    
    def is_pair(self, c1, c2) -> bool:
        return self.get_partner(c1) == c2
     
    def get_index(self, c) -> int:
        if self.is_char_opener(c):
            return self.opening_parentheses.index(c)
        elif self.is_char_closer(c):
            return self.closing_parentheses.index(c)
        
    def get_partner(self, c) -> str:
        '''
        Two-way mapping for parenthesis \n 
        self.get_partner('(') -> ')' \n
        self.get_partner('}') -> '{' 
        '''
        i = self.get_index(c)
        return [r for r in [self.opening_parentheses[i], self.closing_parentheses[i]] if r != c][0]
        
    def score(self, c) -> int:
        i = self.get_index(c)
        return self.scores[i]
        
    def ac_char_score(self, c) -> int:
        i = self.get_index(c)
        return self.ac_char_scores[i]
    
    def error_msg(self, c):
        expected = f'{self.get_partner(c)}' if c else 'opening parenthesis'
        return f'Expected {expected}, but found {c} instead.'
    
    def autocomplete(self, openers):
        return ''.join(reversed([self.get_partner(c) for c in openers]))
    
    def autocomplete_score(self, autocomplete):
        result = self.ac_char_score(autocomplete[0])
        for i, c in enumerate(autocomplete):
            if i > 0:
                result *= 5
                result += self.ac_char_score(c)
        return result
    
@dataclass  
class Day10Solution(Solution):
    program: list = field(default_factory = list)
    syntax_checker: Lang = field(default_factory = Lang)
    results: list = field(default_factory= list)
    
    def __post_init__(self):
        self.program = self.raw_input()
        self.results = [res for res in [self.syntax_checker.check_line(line) for line in self.program]]
    
    def solve_part1(self):
        return array([res.score for res in self.results]).sum()
    
    def solve_part2(self):
        ac_scores = sorted([r.autocomplete_score for r in self.results if r.autocomplete])
        mid = int(len(ac_scores) / 2)
        return ac_scores[mid]
    
    def check_line(self, line) -> Status:
        return self.syntax_checker.check_line(line)

