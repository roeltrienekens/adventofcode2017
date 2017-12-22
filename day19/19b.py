import string

# TODO: Tons of stuffs to optimize, for example on a character or | or - we can just continue on in the same direction.
# TODO: Only on the + do we need logic.

maze = {}

max_row = 0
max_col = 0

steps = 0

for i in range(500):
    for j in range(500):
        maze[(i, j)] = ' '

def read_maze():
    global max_col
    global max_row
    puzzle = open("inputfile.txt", 'r').read().splitlines()
    for row in range(len(puzzle)):
        max_row = max(row, max_row)
        line = list(puzzle[row] + " ")
#        print(line)
        for col in range(len(line)):
            maze[(row, col)] = line[col]
            max_col = max(col, max_col)
    print(max_row)
    print(max_col)


def find_start():
    print("Do you see me?")
    print(max_col)
    for col in range(max_col):
        print(col)
        print(maze[(0, col)])
        if maze[(0, col)] == '|':
            print(col)
            return (0, col)

def find_next(row, col, dir):
    global steps
    steps += 1
    print("After " + str(steps) + " steps we are at [" + str(row) + ", " + str(col) + "] on a " + maze[(row, col)] + " and going " + dir )

    if dir == 'down':
        next = maze[(row + 1, col)]
        if next in list(string.ascii_uppercase + "|-"):
            return (row + 1, col, 'down')
        elif next == '+':
            if maze[(row + 1, col + 1)] in list(string.ascii_uppercase + "|-"):
                return (row + 1, col, 'right')
            else:
                return (row + 1, col, 'left')
    if dir == 'up':
        next = maze[(row - 1, col)]
        if next in list(string.ascii_uppercase + "|-"):
            return (row - 1, col, 'up')
        elif next == '+':
            if maze[(row - 1, col + 1)] in list(string.ascii_uppercase + "|-"):
                return (row - 1, col, 'right')
            else:
                return (row - 1, col, 'left')
    if dir == 'left':
        next = maze[(row, col - 1)]
        if next in list(string.ascii_uppercase + "|-"):
            return (row, col - 1, 'left')
        elif next == '+':
            if maze[(row - 1, col - 1)] in list(string.ascii_uppercase + "|-"):
                return (row, col - 1, 'up')
            else:
                return (row, col - 1, 'down')
    if dir == 'right':
        next = maze[(row, col + 1)]
        if next in list(string.ascii_uppercase + "|-"):
            return (row, col + 1, 'right')
        elif next == '+':
            if maze[(row - 1, col + 1)] in list(string.ascii_uppercase + "|-"):
                return (row, col + 1, 'up')
            else:
                return (row, col + 1, 'down')


#print(list(string.ascii_uppercase + "|-"))
read_maze()
(row, col) = find_start()
dir = 'down'
while (row != -100):
    (row, col, dir) = find_next(row, col, dir)


