def solve_part1(filename):
    lines = get_lines(filename)

    return count_inc(lines)

def solve_part2(filename):
    lines = get_lines(filename)
    sliding_windows = [lines[i] + lines[i+1] + lines[i+2] for (i, l) in enumerate(lines[:-2])]
    
    return count_inc(sliding_windows)

def get_lines(filename):
    f = open(filename)
    lines = [int(l) for l in f]
    f.close()

    return lines

def count_inc(lines):
    prev = -1
    increases = 0
    for line in lines:
        if prev > 0 and line > prev:
            increases += 1
        prev = line

    return increases

if __name__ == '__main__':
    print(solve_part1('example_sweep.txt'))
    print(solve_part2('example_sweep.txt'))