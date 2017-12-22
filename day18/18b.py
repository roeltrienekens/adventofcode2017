import string

DEBUG = True

regs_a = {}
regs_b = {}
for i in range(0, 26):
    regs_a[string.ascii_lowercase[i]] = 0
    regs_b[string.ascii_lowercase[i]] = 0

count = 0

stack_a = []
stack_b = []

def parse_instr(regs, rec_stack, send_stack, instr, do_count):
    global count
    offset = 1
    operand = instr.split(' ')
    if operand[0] == 'snd':
        if do_count:
            count += 1
#        print(instr)
        if operand[1] >= 'a':
            print(send_stack[len(send_stack)-3:])
            send_stack.append(regs[operand[1]])
            print(send_stack[len(send_stack)-3:])
        else:
            send_stack.append(int(operand[1]))
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
#        print(instr)
        if len(rec_stack) > 0:
            print(rec_stack[0:5])
            regs[operand[1]] = rec_stack.pop(0)
            print(rec_stack[0:5])
        else:
            return (True, 0)
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
    return (False, offset)

pc_a = 0
pc_b = 0

lines = open("inputfile.txt", 'r').read().splitlines()
wait_a = False
wait_b = False

terminated_a = False
terminated_b = False
first = True

while (len(stack_a) != 0 or len(stack_b) != 0 or first) and not (terminated_a and terminated_b):
    first = False

    #   Run A until our rcv queue is empty
    print("Continuing with A")
    wait_b = False
    while terminated_a == False and wait_a == False:
        (wait_a, offset) = parse_instr(regs_a, stack_b, stack_a, lines[pc_a], True)
        pc_a += offset
        if pc_a < 0 or pc_a >= len(lines):
            terminated_a = True
    print(count)

    #   Run B until our rcv queue is empty
    print("Continuing with B")
    wait_a = False
    while terminated_b == False and wait_b == False:
        (wait_b, offset) = parse_instr(regs_b, stack_a, stack_b, lines[pc_b], False)
        pc_b += offset
        if pc_b < 0 or pc_b >= len(lines):
            terminated_b = True

    #   A bunch of debugging stuff
    if DEBUG:
        print(str(len(stack_a)) + ", " + str(len(stack_b)))
        print(stack_a)
        print(stack_b)
        if terminated_a:
            print("A Terminated, PC is at " + str(pc_a))
        else:
            print("Current instruction of A is " + lines[pc_a])
        if terminated_b:
            print("B Terminated, PC is at " + str(pc_b))
        else:
            print("Current instruction of B is " + lines[pc_b])

    #   Then repeat until both queues are empty or both programs are terminated

if DEBUG:
    print(stack_a)
    print(stack_b)
    print(count)        # This gives the correct answer for any test input
print(count / 2)        # This appears to give the correct answer for my puzzle input