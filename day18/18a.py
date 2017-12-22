import string

regs = {}
for i in range(0, 26):
    regs[string.ascii_lowercase[i]] = 0

last_played = 0

def parse_instr(instr):
    global last_played
    offset = 1
    operand = instr.split(' ')
    print(instr)
    if operand[0] == 'snd':
        if operand[1] >= 'a':
            last_played = regs[operand[1]]
            print(regs[operand[1]])
        else:
            last_played = int(operand[1])
            print(int(operand[1]))
    elif operand[0] == 'set':
        if operand[2] >= 'a':
            regs[operand[1]] = regs[operand[2]]
        else:
            regs[operand[1]] = int(operand[2])
    elif operand[0] == 'add':
        if operand[2] >= 'a':
            regs[operand[1]] += regs[operand[2]]
        else:
            regs[operand[1]] += int(operand[2])
    elif operand[0] == 'mul':
        if operand[2] >= 'a':
            regs[operand[1]] *= regs[operand[2]]
        else:
            regs[operand[1]] *= int(operand[2])
    elif operand[0] == 'mod':
        if operand[2] >= 'a':
            regs[operand[1]] %= regs[operand[2]]
        else:
            regs[operand[1]] %= int(operand[2])
    elif operand[0] == 'rcv':
        if operand[1] >= 'a':
            if regs[operand[1]] != 0:
                return -9999999999
        else:
            if int(operand[1]) != 0:
                return -9999999999
    elif operand[0] == 'jgz':
        if operand[1] >= 'a':
            if regs[operand[1]] > 0:
                if operand[2] >= 'a':
                    offset = regs[operand[2]]
                else:
                    offset = int(operand[2])
        else:
            if int(operand[1]) > 0:
                if operand[2] >= 'a':
                    offset = regs[operand[2]]
                else:
                    offset = int(operand[2])
    return offset

pc = 0

lines = open("inputfile.txt", 'r').read().splitlines()
while pc >= 0 and pc <= len(lines):
    pc += parse_instr(lines[pc])

print(last_played)