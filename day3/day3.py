def solve_part1(filename):
    lines = readlines(filename)
    sums = []

    for line in lines:
        sums = [int(b) for b in line] if len(sums) == 0 else [sums[i] + int(b) for (i, b) in enumerate(line)]
    
    gamma = ''.join(['1' if s > len(lines) / 2 else '0' for s in sums])

    return get_power_consumption(gamma)

def solve_part2(filename):
    lines = readlines(filename)
    return scrub_diag_report(lines, filter_for_oxygen_rating)*scrub_diag_report(lines, filter_for_carbon_dioxide_rating)

def readlines(filename):
    f = open(filename)
    lines = [l.strip() for l in f.readlines()]
    f.close()

    return lines

def get_power_consumption(gamma):
    epsilon=''.join(['0' if int(b) else '1' for b in gamma])
    return int(gamma, 2)*int(epsilon, 2)

def scrub_diag_report(lines, filter, pos=0):
    if len(lines) <= 1:
        return int(lines[0], 2)
    else:
        bit_sum = sum([int(l[pos]) for l in lines])
        reduce_lines = [l for l in lines if l[pos] == filter(bit_sum, len(lines))]

        return scrub_diag_report(reduce_lines, filter, pos+1)

def filter_for_oxygen_rating(bit_sum, length):
    return str(int(bit_sum >= length / 2))

def filter_for_carbon_dioxide_rating(bit_sum, length):
    return str(int(not (bit_sum >= length / 2)))