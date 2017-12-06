inputfile = "in5a.txt"
testfile = "in5a_test.txt"

import unittest

bank = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
memsize = len(bank)
hash_list = {}

def get_state_hash(state):
    state_hash = 0
    for i in range(0, memsize):
        state_hash += (100 ** i) * state[i]
    return state_hash

def add_state(state_hash):
    if hash_list.has_key(state_hash):
        return True
    else:
        hash_list[state_hash] = 1
        return False

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
    found_old = False

    while(not(found_old)):
        redistribute()
        count += 1
        found_old = add_state(get_state_hash(bank))
    return count

# Unit tests

class MyTest(unittest.TestCase):
    def test(self):

        global hash_list
        hash_list.clear()
        global bank
        bank = [0, 2, 7, 0]
        global memsize
        memsize = len(bank)
        self.assertEqual(calc_steps(), 5)


if __name__ == '__main__':

    print("The number of steps is " + str(calc_steps()))

    unittest.main()
