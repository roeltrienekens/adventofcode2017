inputfile = "input.txt"

delay = 0
done = False
severity = 0

while done == False:
    done = True
    delay += 1
    for line in open(inputfile, 'r'):
        layer = int(line.replace(':', '').split()[0])
        depth = int(line.split()[1])
        if layer % (2 * (depth - 1)) == 0:
            severity += layer * depth

print(severity)

