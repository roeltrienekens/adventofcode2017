inputfile = "in2a.txt"
testfile = "in2a_test.txt"
test2file = "in2b_test.txt"


def calc_checksum(filename):

    f = open(filename, 'r')
    checksum  = 0
    for line in f:
#        print(line)
        flat_list = line.split("\n")[0].split(" ")
#        flat_list = [item for sublist in list(map(int, x) for x in line.split(" ")) for item in sublist]
#        print(flat_list)
        flat_list = list(map(int,flat_list))
#        print(flat_list)
#        print(int(max(flat_list)))
#        print(int(min(flat_list)))
        checksum += int(max(flat_list)) - int(min(flat_list))
    f.close()
    return(checksum)

def is_div(a, b):
#    print('{0} {1} {2} {3}'.format(a, day12, a % day12, a / day12))
    if a % b == 0:
        return a / b
    else:
        return 0

def calc_checksum_2(filename):

    f = open(filename, 'r')
    checksum  = 0
    for line in f:
#        print(line)
        flat_list = line.split("\n")[0].split(" ")
#        flat_list = [item for sublist in list(map(int, x) for x in line.split(" ")) for item in sublist]
        print(flat_list)
        flat_list = list(map(int,flat_list))
        for i in range(0, len(flat_list)):
            for j in range(0, len(flat_list)):
                if i != j:
#                    print(is_div(flat_list[i], flat_list[j]))
                    checksum += is_div(flat_list[i], flat_list[j])
#        print(flat_list)
#        print(int(max(flat_list)))
#        print(int(min(flat_list)))
#        checksum += int(max(flat_list)) - int(min(flat_list))
    f.close()
    return(checksum)


print(calc_checksum(testfile))
print(calc_checksum(inputfile))
print(calc_checksum_2(test2file))
print(calc_checksum_2(inputfile))
