def solve_part1(filename):
    depth=0 
    horiz=0

    f = open(filename)
    for l in f:
        direction = l.split()[0]
        displacement = int(l.split()[1])

        match direction:
            case 'forward':
                horiz+=displacement
            case 'down':
                depth+=displacement
            case 'up':
                depth-=displacement
    f.close()

    return depth*horiz

def solve_part2(filename):
    depth=0 
    horiz=0
    aim=0

    f = open(filename)
    for l in f:
        direction = l.split()[0]
        displacement = int(l.split()[1])

        match direction:
            case 'forward':
                horiz+=displacement
                depth+=aim*displacement
            case 'down':
                aim+=displacement
            case 'up':
                aim-=displacement
    f.close()

    return depth*horiz