TEST = False

if TEST:
    inputfile = "input_test.txt"
else:
    inputfile = "input.txt"

HASHLENGTH = 256

LAST_INDEX = HASHLENGTH - 1
hashlist = range(0, HASHLENGTH)
cursor = 0
skip = 0


def reverse(sublist):
    reversed_list = []
    for i in range(0, len(sublist)):
        reversed_list.append(sublist[len(sublist) - 1 - i])
    return reversed_list


def reverse_circular_sublist(length):
    global cursor
    global skip
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


def calc_dense_hash(index):
    ans = hashlist[index]
    for i in range(index + 1, index + 16):
        ans = ans ^ hashlist[i]
    return ans

def hash_knot(key):
    dense_hash = ""
    for i in range(64):
        for c in key:
            length = ord(c)
            reverse_circular_sublist(int(length))
        for length in (17, 31, 73, 47, 23):
            reverse_circular_sublist(int(length))
    for i in range(16):
        dense_hash += "{0:0{1}x}".format(calc_dense_hash(i * 16), 2)
    return dense_hash

for line in open(inputfile, 'r'):
    print(hash_knot(line))
