def solve_part1(filename):
    return solve(filename, part1=True)

def solve_part2(filename):
    return solve(filename)

def readlines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def solve(filename, part1=False):
    inp = [int(s) for s in readlines(filename)[0].split(',')]
    size = max(inp) + 1
    model = [inp.count(i) for i in range(size)]
    dists = [i for i in range(size)]
    if not part1: 
        for (i, _) in enumerate(dists):
            dists[i] = i + dists[i-1] if i > 0 else 0
    to_push = [d for d in dists[1:]]

    result = []
    for i in range(size):
        result.append(sum([m * d for (m,d) in zip(model, dists)]))
        if i < len(to_push): dists = [to_push[i]] + dists
        dists.pop()
    return min(result)