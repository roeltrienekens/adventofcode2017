inputfile = "in5a.txt"
testfile = "in5a_test.txt"

import unittest

bank = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
memsize = len(bank)
hash_list = {}
t = 0

def get_state_hash(state):
    state_hash = 0
    for i in range(0, memsize):
        state_hash += (100 ** i) * state[i]
    return state_hash

def add_state(state_hash):
    global t
    if hash_list.has_key(state_hash):
        return t - hash_list[state_hash]
    else:
        hash_list[state_hash] = t
        t += 1
        return 0

def redistribute():
    max_bank = 0
    max_index = -1
    for i in range(0, memsize):
        if bank[i] > max_bank:
            max_bank = bank[i]
            max_index = i
    blocks = bank[max_index]
    bank[max_index] = 0
    next_index = (max_index + 1) % memsize
    while(blocks > 0):
        bank[next_index] += 1
        blocks -= 1
        next_index = (next_index + 1) % memsize

def calc_steps():
    count = 0
    found_old = 0

    while(found_old == 0):
        redistribute()
        count += 1
        found_old = add_state(get_state_hash(bank))
    return found_old

# Unit tests

class MyTest(unittest.TestCase):
    def test(self):

        global hash_list
        hash_list.clear()
        global bank
        bank = [0, 2, 7, 0]
        global memsize
        memsize = len(bank)
        self.assertEqual(calc_steps(), 4)


if __name__ == '__main__':

    print("The size of the loop is " + str(calc_steps()))

    unittest.main()
