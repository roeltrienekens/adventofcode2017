

particles = {}

lines = open("inputfile.txt", 'r').read().splitlines()

for i in range(len(lines)):
    particles[i] = lines[i].replace('a=<','>').split('>')[3].split(',')

# Get the Manhattan distance of the acceleration vector

def acc(vector):
    return abs(int(vector[0])) + abs(int(vector[1])) + abs(int(vector[2]))

min_acc = 999999999
part_no = -1

# The particles with the smalles acceleration is the one that in the end will remain closest

for i in range(len(lines)):
    if acc(particles[i]) < min_acc:
        min_acc = acc(particles[i])
        part_no = i

print part_no
