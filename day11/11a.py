inputfile = "input.txt"

def move(x, y, direction):
    if direction == "n":
        return (x, y + 1)
    elif direction == "nw":
        return (x + 1, y)
    elif direction == "sw":
        return (x + 1, y - 1)
    elif direction == "s":
        return (x, y - 1)
    elif direction == "se":
        return (x - 1, y)
    elif direction == "ne":
        return (x - 1, y + 1)

def distance(x1, y1, x2, y2):
    diag = min(abs(x1 - x2), abs(y1 - y2))
    straight = max(abs(x1 - x2) - diag, abs(y1 - y2) - diag)
    return (diag + straight)

x = 0
y = 0
max_distance = 0
for line in open(inputfile, 'r'):
    for step in line.split(","):
        (x, y) = move(x, y, step)
        max_distance = max(max_distance, distance(x, y, 0, 0))

print("He ends up " + str(distance(x, y, 0, 0)) + " hexes away.")
print("The furthest he was ever away was " + str(max_distance) + " hexes." )
