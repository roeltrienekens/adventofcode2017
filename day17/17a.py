import unittest

buffer = [ 0 ]
cursor = 0

def insert_at_position(buffer, value, pos):
    buffer.insert((pos % len(buffer)) + 1, value)
    return buffer


class insert_at_position_test(unittest.TestCase):
    def test(self):
        self.assertListEqual([0, 2, 1], insert_at_position([0, 1], 2, 0))
        self.assertListEqual([0, 2, 1], insert_at_position([0, 1], 2, 2))
        self.assertListEqual([0, 2, 1], insert_at_position([0, 1], 2, 4))

if __name__ == '__main__':
    buffer = [0]
    cursor = 0
    step = 348

    for i in range(1, 2018):
        cursor = ((cursor + step) % len(buffer)) + 1
        insert_at_position(buffer, i, cursor - 1)
#        print(buffer)
#        print(cursor)

print(buffer[cursor - 3: cursor + 3])
    #unittest.main()


