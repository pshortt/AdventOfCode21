import numpy as np

def solve_part1(filename):
    return solve(filename, part1=True)

def solve_part2(filename):
    return solve(filename)

def readlines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def solve(filename, part1=False):
    file_content = [s.split(' | ') for s in readlines(filename)]
    file_content = [[s.split(' ') for s in line] for line in file_content]
    [wire_configs, output_signals] = [[a[i] for a in file_content] for (i,_) in enumerate(file_content[0])]
    if part1:
        return count_unique_values(output_signals)
    else:
        return output_sum(wire_configs, output_signals)

def count_unique_values(output_signals):
    unique_signals = [[s for s in out if len(s) in unique_lengths()] for out in output_signals]
    return np.array([len(us) for us in unique_signals]).sum()

def output_sum(wire_configs, output_signals):
    output_signals = [np.array([decode(w, o)]).sum() for (w, o) in zip(wire_configs, output_signals)]
    return np.array([output_signals]).sum()

def decode(wire_config, output_signal):
    [one_wiring, seven_wiring, four_wiring, eight_wiring] = get_unique_wires(wire_config)
    num_occurances = {sum([s.count(c) for s in wire_config]) : c for c in  one_pass_eight()}
    wire_map = ''

    for c in one_pass_eight():
        match c:
            case 'b':
                wire_map += num_occurances.get(6)
            case 'e':
                wire_map += num_occurances.get(4)
            case 'f':
                wire_map += num_occurances.get(9)
            case 'c':                
                wire_map += not_and(wire_map, 'f', one_wiring)
            case 'a':
                wire_map += not_and(wire_map, 'cf', seven_wiring)
            case 'd':
                wire_map += not_and(wire_map, 'bcf', four_wiring)
            case 'g':
                wire_map += not_and(wire_map, 'abcdef', eight_wiring)

    result_signal = [''.join(sorted([translate_wire(c, wire_map) for c in sig])) for sig in output_signal]
    return int(''.join([signal_to_digit(sig) for sig in result_signal]))

def unique_lengths():
    return [2, 3, 4, 7]

def one_pass_eight(): # representation of '8' designed to decode the wires in one pass
    return 'befcadg'

def get_unique_wires(wire_config):
    return sorted([w for w in wire_config if len(w) in unique_lengths()], 
        key=lambda s : len(s))

def not_and(wire_map, s, w):
    for c in w:
        if c not in [translate_wire(x, wire_map, False) for x in s]:
            return c
    
def translate_wire(c, wire_map, return_og=True):
    for (og, w) in zip(one_pass_eight(), wire_map):
        if c == w and return_og:
            return og
        elif c == og and not return_og:
            return w

def signal_to_digit(signal):
    match signal:
        case 'abcefg':
            return '0'
        case 'cf':
            return '1'
        case 'acdeg':
            return '2'
        case 'acdfg':
            return '3'
        case 'bcdf':
            return '4'
        case 'abdfg':
            return '5'
        case 'abdefg':
            return '6'
        case 'acf':
            return '7'
        case 'abcdefg':
            return '8'
        case 'abcdfg':
            return '9'