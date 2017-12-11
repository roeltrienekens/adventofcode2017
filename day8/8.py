import string
import operator

inputfile = "input.txt"
testfile = "input_test.txt"

reg = {}        # Registers and the values they are holding

def execute(instr):
    op = line.split()
    if (eval(op[4:])):
        if (op[1] == 'inc'):
            reg[op[0]] += int(op[2])
        elif (op[1] == 'dec'):
            reg[op[0]] -= int(op[2])

def eval(cond):
    if (cond[1] == '>'):
        return reg[cond[0]] > int(cond[2])
    elif (cond[1] == '>='):
        return reg[cond[0]] >= int(cond[2])
    elif (cond[1] == '<'):
        return reg[cond[0]] < int(cond[2])
    elif (cond[1] == '<='):
        return reg[cond[0]] <= int(cond[2])
    elif (cond[1] == '=='):
        return reg[cond[0]] == int(cond[2])
    elif (cond[1] == '!='):
        return reg[cond[0]] != int(cond[2])
    else:
        print('Unknown conditional operator in ' + str(cond))

if __name__ == '__main__':

    for i in string.ascii_lowercase[:26]:
        reg[i] = 0

    for i in string.ascii_lowercase[:26]:
        for j in string.ascii_lowercase[:26]:
            reg[i + j] = 0

    for i in string.ascii_lowercase[:26]:
        for j in string.ascii_lowercase[:26]:
            for k in string.ascii_lowercase[:26]:
                reg[i + j + k] = 0

    highest = 0

    for line in open(inputfile, 'r'):
        execute(line)
        highest = max(highest, max(reg.iteritems(), key=operator.itemgetter(1))[1])

    print("Highest final register is " + str(max(reg.iteritems(), key=operator.itemgetter(1))[1]))
    print("Highest intermediate register value is " + str(highest))

