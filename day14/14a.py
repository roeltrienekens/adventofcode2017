INPUT = 'stpzcrnm'
HASHLENGTH = 256

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

grid = {}

total = 0
for i in range(128):
    for c in (hash_knot(INPUT + "-" + str(i))):
        if (c == '0'):
            total += 0
        elif (c in ('1', '2', '4', '8')):
            total += 1
        elif (c in ('3', '5', '6', '9', 'a', 'c')):
            total += 2
        elif (c in ('7', 'b', 'd', 'e')):
            total += 3
        else: # (c in ('f')):
            total += 4
print(total)

#print(hash_knot("18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"))