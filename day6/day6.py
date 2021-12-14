def solve_part1(filename):
    return solve(filename, True)

def solve_part2(filename):
    return solve(filename)

def readlines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def solve(filename, part1=False):
    model = [0 for _ in range(9)] 
    for i in [int(s) for s in readlines(filename)[0].split(',')]: model[i] += 1
    for _ in range(80 if part1 else 256):
        spawn = model.pop(0)
        model.append(spawn)
        model[6] += spawn
    return sum(model)