import sys
from z3 import *

def main():
    if len(sys.argv) < 2:
        print "usage: python solver.py <path_to_file>"
        exit(0)

    with open(sys.argv[1], "rb") as f:
        data = [x.strip() for x in f.read().split()]

    # Seperate out data
    grid = []
    for x in data:
        grid.extend((int(y) for y in list(x)))

    variables = []
    for x in range(81):
        variables.append(Int("x%s" % x))

    s = Solver()

    # Add constraints
    x = 0
    while x < 81:

        if grid[x] > 0:
            # This must be a constant
            s.add(variables[x] == grid[x])
        else:

            # Upper and lower bounds
            s.add(variables[x] < 10)
            s.add(variables[x] > 0)

            # Check same row
            rowstart = (x - (x % 9))
            for y in range(9):
                if (rowstart+y != x):
                    s.add(variables[x] != variables[rowstart+y])

            # Check same column
            colstart = x % 9
            y = 0
            while y < 81:
                if (colstart+y != x):
                    s.add(variables[x] != variables[colstart+y])
                y = y + 9

            # Get the top left of our current square
            topleft = x - (x % 3)
            colstart = (topleft % 9)
            while colstart <= topleft:
                colstart = colstart + 27

            topleft = (colstart - 27)
            updates = [topleft, topleft+1, topleft+2, topleft+9, topleft+10, topleft+11, topleft+18, topleft+19, topleft+20]
            for y in updates:
                if y != x:
                    s.add(variables[x] != variables[y])

        x = x + 1

    s.check()
    # for c in s.assertions():
    #     print c
    m = s.model()

    # print m

    for x in range(81):
        sys.stdout.write(repr(m[variables[x]]))
        if (x % 9 == 8):
            print ""

if __name__ == '__main__':
    main()
