import sys

INPUT = 'stpzcrnm'
#INPUT = 'flqrgnkx'
HASHLENGTH = 256

# This is all a copy from Day 10 until i find out / can be bothered to checks out how imports or includes work

def reverse(sublist):
    reversed_list = []
    for i in range(0, len(sublist)):
        reversed_list.append(sublist[len(sublist) - 1 - i])
    return reversed_list


def reverse_circular_sublist(hashlist, length, cursor, skip):
    if (cursor + length) < HASHLENGTH:
        hashlist[cursor:cursor + length] = reverse(hashlist[cursor:cursor + length])
    else:
        length1 = HASHLENGTH - cursor
        length2 = length - length1
        reversed_list = reverse(hashlist[cursor:HASHLENGTH] + hashlist[0:length2])
        hashlist[cursor:HASHLENGTH] = reversed_list[0:length1]
        hashlist[0:length2] = reversed_list[length1:length]
    cursor = (cursor + length + skip) % HASHLENGTH
    skip += 1
    return cursor, skip


def calc_dense_hash(hashlist, index):
    ans = hashlist[index]
    for i in range(index + 1, index + 16):
        ans = ans ^ hashlist[i]
    return ans

def hash_knot(key):
    dense_hash = ""
    hashlist = range(0, HASHLENGTH)
    cursor = 0
    skip = 0
    for i in range(64):
        for c in key:
            length = ord(c)
            (cursor, skip) = reverse_circular_sublist(hashlist, int(length), cursor, skip)
        for length in (17, 31, 73, 47, 23):
            (cursor, skip) = reverse_circular_sublist(hashlist, int(length), cursor, skip)
    for i in range(16):
        dense_hash += "{0:0{1}x}".format(calc_dense_hash(hashlist, i * 16), 2)
    return dense_hash

# Start day 14 code

# initialize the grid

grid = {}

for i in range(128):
    for j in range(128):
        grid[(i,j)] = 0

# build the grid
for i in range(128):
    x = 0
    key = INPUT + "-" + str(i)
    print(key)
    for c in (hash_knot(key)):
        if (c in ('1', '3', '5', '7', '9', 'b', 'd', 'f')):
            grid[(i, (x * 4) + 3)] = 1
        if (c in ('2', '3', '6', '7', 'a', 'b', 'e', 'f')):
            grid[(i, (x * 4) + 2)] = 1
        if (c in ('4', '5', '6', '7', 'c', 'd', 'e', 'f')):
            grid[(i, (x * 4) + 1)] = 1
        if (c in ('8', '9', 'a', 'b', 'c', 'd', 'e', 'f')):
            grid[(i, (x * 4))] = 1
        x += 1

def mark_area(x, y, num):
    grid[(x, y)] = num
    if (x - 1) >= 0:
        if grid[(x - 1, y)] == 1:
            mark_area(x - 1, y, num)
    if (x + 1) < 128:
        if grid[(x + 1, y)] == 1:
            mark_area(x + 1, y, num)
    if (y - 1) >= 0:
        if grid[(x, y - 1)] == 1:
            mark_area(x, y - 1, num)
    if (y + 1) < 128:
        if grid[(x, y + 1)] == 1:
            mark_area(x, y + 1, num)

count = 2       # because 0 and 1 already denote empty and new bits, respectively
for i in range(128):
    for j in range(128):
        if grid[(i, j)] == 1:
            count = (count + 1)
            mark_area(i, j, count)

# Validation function that checks if there are no directly touching groups.
# And while it's at it, counts how many different groups it encounters.

def check_area():
    seen = set()
    for x in range(0, 128):
        for y in range(0, 128):
            check = grid[(x, y)]
            if check == 0:
                continue
            seen.add(check)
            if x > 0:
                if grid[(x - 1, y)] not in (check, 0):
                    print("Problem at " + str(x) + ", " + str(y))
            if x < 127:
                if grid[(x + 1, y)] not in (check, 0):
                    print("Problem at " + str(x) + ", " + str(y))
            if y > 0:
                if grid[(x, y - 1)] not in (check, 0):
                    print("Problem at " + str(x) + ", " + str(y))
            if y < 127:
                if grid[(x, y + 1)] not in (check, 0):
                    print("Problem at " + str(x) + ", " + str(y))
    print(len(seen))

# Print the grid for fun. And debugging purposes. Sort of.

for i in range(128):
    for j in range(128):
        sys.stdout.write(str(grid[(i, j)]))
    sys.stdout.write('\n')
    sys.stdout.flush()

# This is the number that the final group has. Since we started at 2, this should be 2 higher than the solution.

print(count)

check_area()

# As a quick check, this should be 23234babdc6afa036749cfa9b597de1b

print(hash_knot("18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"))
print('23234babdc6afa036749cfa9b597de1b')