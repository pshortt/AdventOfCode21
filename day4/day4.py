def solve_part1(filename):
    game = BingoGame(readlines(filename), 1)
    result = game.run()
    return result

def solve_part2(filename):
    game = BingoGame(readlines(filename), 2)
    result = game.run()
    return result

def readlines(filename):
    f = open(filename)
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines

class BingoGame():
    def __init__(self, bingo_system_output, part):
        self.draw = bingo_system_output.pop(0).split(',')
        boards_text = [bingo_system_output[x*5 + x + 1 : x*5 + x + 6] for x in range(int(len(bingo_system_output) / 6))]
        self.boards = [BingoBoard(b) for b in boards_text]
        self.winning_boards = []
        if part == 1:
            self.result_index = 0
        else:
            self.result_index = len(self.boards) - 1
    
    def call_number(self, number):
        for board in self.boards: 
            if not board.winner: 
                board.check(number)
                if board.winner:
                    self.winning_boards.append(board)

    def run(self):
        for number in self.draw:
            if not all([board.winner for board in self.boards]):
                self.call_number(number)
        
        return self.winning_boards[self.result_index].score
        
class BingoBoard():
    def __init__(self, board):
        self.rows = [[BingoCell(number) for number in r.split()] for r in board]
        self.winner = False
        self.score = 0

    def check(self, number):
        for row in self.rows:
            for cell in row: 
                if cell.number == number: cell.mark()        
        self.winner = self.check_rows() or self.check_cols()
        self.set_score(number)

    def check_rows(self):
        return any(all(cell.marked for cell in row) for row in self.rows)

    def check_cols(self):
        cols = []
        for i in range(len(self.rows[0])):
            cols.append([row[i] for row in self.rows])

        return any(all(cell.marked for cell in col) for col in cols)

    def set_score(self, number):
        if self.winner:
            result = sum([sum([int(cell.number) for cell in row if not cell.marked]) for row in self.rows])
            self.score = result*int(number)
    
    def __str__(self):
        return '\n'.join([' '.join(['(' + cell.number + ')' if cell.marked else ' ' + cell.number + ' ' for cell in row]) for row in self.rows])


class BingoCell():
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True