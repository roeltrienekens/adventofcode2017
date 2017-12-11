

inputfile = "input.txt"

for line in open(inputfile, 'r'):
    current_group = 0
    total = 0
    in_garbage = False
    garbage_count = 0
    bla = 0
    skip = False
    for c in line:
        print(c + str(total))
        if skip == True:            # previous char was a '!'
            skip = False
        elif c == '>':              # closes garbage
            in_garbage = False
        elif c == '!':
            skip = True
#        elif in_garbage:            # do nothing
#            pass
        elif c == '{':              # opens a new group
            if in_garbage:
                garbage_count += 1
            else:
                current_group += 1
        elif c == '<':              # starts garbage
            if in_garbage:
                garbage_count += 1
            else:
                in_garbage = True
        elif c == '}':
            if in_garbage:
                garbage_count += 1
            else:
                total += current_group
                current_group -= 1
        else:
            if in_garbage:
                garbage_count += 1

    print(total)
    print(garbage_count)
