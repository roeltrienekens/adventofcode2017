import unittest

inputfile = "in5a.txt"
testfile = "in5a_test.txt"

instr = []

def read_instr(inputfile):
    f = open(inputfile, 'r')
    for line in f:
        instr.append(int(line))

def jump_inc_dec(instr, loc):
    new_loc = loc + instr[loc]
    if instr[loc] < 3:
        instr[loc] += 1
    else:
        instr[loc] -= 1
    return new_loc

def isExit(instr, loc):
    if (loc + instr[loc] > (len(instr) - 1)):
        return True
    else:
        return False

def traverse(instr): #, mode):
    steps = 0
    loc = 0
    while isExit(instr, loc) == False:
        loc = jump_inc_dec(instr, loc)
        steps += 1
    return steps + 1

# Unit tests

class MyTest(unittest.TestCase):
    def test(self):

        test_instr = [0, 3, 0, 3, -3]
        self.assertFalse(isExit(test_instr, 0))
        self.assertFalse(isExit(test_instr, 1))
        self.assertFalse(isExit(test_instr, 2))
        self.assertTrue(isExit(test_instr, 3))
        self.assertFalse(isExit(test_instr, 4))

if __name__ == '__main__':

    read_instr(inputfile)
    print(traverse(instr)) #, mode))

    unittest.main()
