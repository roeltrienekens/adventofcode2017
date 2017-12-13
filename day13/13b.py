inputfile = "input.txt"

MAX = 4000000

catch = set()

for line in open(inputfile, 'r'):
    (layer, depth) = line.replace(':', '').split()
    catch |= set(range(((-1 * int(layer)) % (2 * (int(depth) - 1))), MAX, (2 * (int(depth) - 1))))

print(set(range(0, MAX)) - catch)


