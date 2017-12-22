
LENGTH = 16




def spin(order, num):
    return order[LENGTH - num: LENGTH] + order[0: LENGTH - num]

def exchange(order, x, y):
    a = min(x, y)
    b = max(x, y)
    return order[0: a] + order[b] + order[a + 1: b] + order[a] + order[b + 1: LENGTH]

def partner(order, a, b):
#    print(order + " " + a + " " + b)
    return exchange(order, order.index(a), order.index(b))

print(exchange('fghijklmnopabcde', 10, 2))

if LENGTH == 5:
    print(spin('abcde', 3))
    print(exchange('abcde', 1, 3))
    print(partner('abcde', 'b', 'd'))

starting_order = "abcdefghijklmnop"
order = starting_order
initial = True
counter = 0

for line in open("inputfile.txt", 'r'):
    while (initial or order != starting_order):
        initial = False
        for move in line.split(','):
#            print(move + " on " + order)
            if move[0] == 's':
                order = spin(order, int(move[1:]))
            elif move[0] == 'x':
                (a, b) = move[1:].split('/')
                order = exchange(order, int(a), int(b))
            elif move[0] == 'p':
                (a, b) = move[1:].split('/')
                order = partner(order, a, b)
        counter += 1

for i in range(1000000000 % counter):
    for line in open("inputfile.txt", 'r'):
        for move in line.split(','):
            if move[0] == 's':
                order = spin(order, int(move[1:]))
            elif move[0] == 'x':
                (a, b) = move[1:].split('/')
                order = exchange(order, int(a), int(b))
            elif move[0] == 'p':
                (a, b) = move[1:].split('/')
                order = partner(order, a, b)

print(order)