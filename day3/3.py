# inputfile = ""
# testfile = ""
# test2file = ""

import unittest

Size = 10
Matrix = [[0 for x in range(2 * Size + 1)] for y in range(2 * Size + 1)]


def init_matrix():
    Matrix = [[0 for x in range(2 * Size + 1)] for y in range(2 * Size + 1)]


def get_coordinates(num):

    x = 0
    y = 0
    res = 0
    ring = 0
    if num == 1:
        return (0, 0)
    while res == 0:         # till we find the answer
#        print("num = {0}, ring = {1}, sum = {2}".format(num, ring, ((ring * 2) - 1) ** 2))
        if num <= (((2 * (ring) + 1) ** 2)):      # we found the right ring
#            print("num = {0}, ring = {1}, sum = {2}".format(num, ring, (((2 * (ring) + 1) ** 2))))

            inner_block = (((2 * (ring - 1)) + 1) ** 2)
#            print(inner_block)

            outer_block = (((2 * (ring + 1)) ** 2))
#            print(outer_block)

            offset = num - inner_block
#            print(offset)
            if offset <= (2 * ring):
                x = ring
                y = offset - ring
            elif offset <= (4 * ring):
                x = (3 * ring) - offset
                y = ring
            elif offset <= (6 * ring):
                x = -1 * ring
                y = (5 * ring) - offset
            else:
                x = offset - (7 * ring)
                y = -1 * ring
#            print(x)
#            print(y)
            res = abs(x) + abs(y)
#            print(res)
        else:
            ring += 1
#    return res
    return(x, y)

def get_value(x, y):
    return Matrix[x + Size][y + Size]

def set_value(x, y, val):
    Matrix[x + Size][y + Size] = val

def get_surround(x, y):
    sum = get_value(x - 1, y)
    sum += get_value(x - 1, y - 1)
    sum += get_value(x, y - 1)
    sum += get_value(x + 1, y - 1)
    sum += get_value(x + 1, y)
    sum += get_value(x + 1, y + 1)
    sum += get_value(x, y + 1)
    sum += get_value(x - 1, y + 1)
    return sum

def day2(puz):
    init_matrix()
    i = 1
    sum = 0
    (x, y) = (0, 0)
#    print("x " + str(x) + " y " + str(y))
    set_value(x, y, 1)
    while sum <= puz:
#        print("sum " + str(sum))
        i += 1
#        print("i " + str(i))
        (x, y) = get_coordinates(i)
#        print("x " + str(x) + " y " + str(y))
        sum = get_surround(x, y)
        print("i " + str(i) + " x " + str(x) + " y " + str(y) + " sum " + str(sum))
        set_value(x, y, sum)
    return sum

# Testcases

class MyTest(unittest.TestCase):
    def test(self):
        (x, y) = get_coordinates(1)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        (x, y) = get_coordinates(2)
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)

        (x, y) = get_coordinates(3)
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

        (x, y) = get_coordinates(4)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

        (x, y) = get_coordinates(5)
        self.assertEqual(x, -1)
        self.assertEqual(y, 1)

        (x, y) = get_coordinates(6)
        self.assertEqual(x, -1)
        self.assertEqual(y, 0)

        (x, y) = get_coordinates(7)
        self.assertEqual(x, -1)
        self.assertEqual(y, -1)

        (x, y) = get_coordinates(8)
        self.assertEqual(x, 0)
        self.assertEqual(y, -1)

        (x, y) = get_coordinates(9)
        self.assertEqual(x, 1)
        self.assertEqual(y, -1)

        (x, y) = get_coordinates(10)
        self.assertEqual(x, 2)
        self.assertEqual(y, -1)

        (x, y) = get_coordinates(11)
        self.assertEqual(x, 2)
        self.assertEqual(y, 0)

if __name__ == '__main__':

#    print(day2(100))
#    print(day2(4))
    print(day2(361527))
    unittest.main()


#print(1)
#print(day2(1))
#print(2)
#print(day2(2))
#print(361527)
#print(day2(361527))



#print(calc_distance(1))     # 0
#print("bla")
#print(calc_distance(12))    # 3
#print("12 -> 3")
#print(calc_distance(23))    # 2
#print("23 -> 2")
#print(calc_distance(83))    # 8
#print("83 -> 8")
#print(calc_distance(1024))  # 31
#print("1024 -> 31")
#print(calc_distance(361527))  # puzzle input (answer = 326)
