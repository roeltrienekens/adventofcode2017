TEST = False

if TEST:
    inputfile = "input_test.txt"
    HASHLENGTH = 5
else:
    inputfile = "input.txt"
    HASHLENGTH = 256

LAST_INDEX = HASHLENGTH - 1
hashlist = range(0,HASHLENGTH)
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
#        print(hashlist[cursor:HASHLENGTH] + hashlist[0:length2])
        reversed_list = reverse(hashlist[cursor:HASHLENGTH] + hashlist[0:length2])
#        print(reversed_list)
#        print(reversed_list[0:length1])
        hashlist[cursor:HASHLENGTH] = reversed_list[0:length1]
        hashlist[0:length2] = reversed_list[length1:length]
    cursor = (cursor + length + skip) % HASHLENGTH
    skip += 1
    print("Cursor at " + str(cursor) + ", skip is " + str(skip))

# print(hashlist)
# cursor = 250
# length = 10
# reverse_circular_sublist(length)
# hashlist[cursor:cursor + int(length)] = reverse(hashlist[cursor:cursor + int(length)])
# print(hashlist)



print(hashlist)
for line in open(inputfile, 'r'):
    print(line)
    for length in line.split(','):
        print(length)
        reverse_circular_sublist(int(length))
        print(hashlist)
print(hashlist)
print(hashlist[0] * hashlist[1])

