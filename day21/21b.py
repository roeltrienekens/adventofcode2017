rules = {}

def get_block(matrix, size, row, col):
    ret_matrix = [['.' for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            ret_matrix[i][j] = matrix[row * size + i][col * size + j]
    return ret_matrix


def set_block(matrix, block, size, row, col):
#    print_matrix(matrix)
#    print block
    for i in range(size):
        for j in range(size):
            matrix[(row * size) + i][(col * size) + j] = hash_to_matrix(block)[i][j]


def matrix_to_hash(matrix):
    hash = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            hash += matrix[i][j]
        if i != len(matrix) - 1:
            hash += '/'
    return hash


def hash_to_matrix(hash):
#    print hash
#    print len(hash)
    if len(hash) == 5:
        ret_matrix = [['.' for x in range(2)] for y in range(2)]
        for i in range(2):
            for j in range(2):
                ret_matrix[i][j] = hash[3 * i + j]
        return ret_matrix
    if len(hash) == 11:
        ret_matrix = [['.' for x in range(3)] for y in range(3)]
        for i in range(3):
            for j in range(3):
                ret_matrix[i][j] = hash[4 * i + j]
        return ret_matrix
    if len(hash) == 19:
        ret_matrix = [['.' for x in range(4)] for y in range(4)]
        for i in range(4):
            for j in range(4):
                ret_matrix[i][j] = hash[5 * i + j]
        return ret_matrix

def print_matrix(matrix):
    hash = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            hash += matrix[i][j]
        print hash
        hash = ''

def rotate(matrix):
    if len(matrix) == 2:
        ret_matrix = [['.' for x in range(2)] for y in range(2)]
        ret_matrix[0][0] = matrix[1][0]
        ret_matrix[0][1] = matrix[0][0]
        ret_matrix[1][1] = matrix[0][1]
        ret_matrix[1][0] = matrix[1][1]
        return ret_matrix
    elif len(matrix) == 3:
        ret_matrix = [['.' for x in range(3)] for y in range(3)]
        ret_matrix[0][0] = matrix[2][0]
        ret_matrix[0][1] = matrix[1][0]
        ret_matrix[0][2] = matrix[0][0]
        ret_matrix[1][2] = matrix[0][1]
        ret_matrix[2][2] = matrix[0][2]
        ret_matrix[2][1] = matrix[1][2]
        ret_matrix[2][0] = matrix[2][2]
        ret_matrix[1][0] = matrix[2][1]
        ret_matrix[1][1] = matrix[1][1]
        return ret_matrix


def mirror(matrix):
    if len(matrix) == 2:
        ret_matrix = [['.' for x in range(2)] for y in range(2)]
        ret_matrix[0][0] = matrix[0][1]
        ret_matrix[0][1] = matrix[0][0]
        ret_matrix[1][0] = matrix[1][1]
        ret_matrix[1][1] = matrix[1][0]
        return ret_matrix
    elif len(matrix) == 3:
        ret_matrix = [['.' for x in range(3)] for y in range(3)]
        ret_matrix[0][0] = matrix[0][2]
        ret_matrix[0][1] = matrix[0][1]
        ret_matrix[0][2] = matrix[0][0]
        ret_matrix[1][0] = matrix[1][2]
        ret_matrix[1][1] = matrix[1][1]
        ret_matrix[1][2] = matrix[1][0]
        ret_matrix[2][0] = matrix[2][2]
        ret_matrix[2][1] = matrix[2][1]
        ret_matrix[2][2] = matrix[2][0]
        return ret_matrix

def read_rules():
    global rules
    lines = open("inputfile.txt", 'r').read().splitlines()
    for i in range(len(lines)):
        line = lines[i].split(' => ')
        # TODO: Add mirror and rotated rules
#        print line[0] + " " + line[1]
        hash = line[0]
        for j in range(4):
#            print hash
            if hash not in rules:
                rules[hash] = line[1]
            mirrored_hash = matrix_to_hash(mirror(hash_to_matrix(hash)))
#            print hash
            if mirrored_hash not in rules:
                rules[mirrored_hash] = line[1]
            hash = matrix_to_hash(rotate(hash_to_matrix(hash)))

def expand(matrix):
    size = len(matrix)
    if size % 2 == 0:
        new_matrix = [['.' for x in range((size / 2) * 3)] for y in range((size / 2) * 3)]
        for i in range(size / 2):
            for j in range(size / 2):
#                print translate_block(get_block(matrix, size, i, j))
                set_block(new_matrix, translate_block(get_block(matrix, 2, i, j)), 3, i, j)
        return new_matrix
    elif size % 3 == 0:
        new_matrix = [['.' for x in range((size / 3) * 4)] for y in range((size / 3) * 4)]
        for i in range(size / 3):
            for j in range(size / 3):
#                print translate_block(get_block(matrix, size, i, j))
                set_block(new_matrix, translate_block(get_block(matrix, 3, i, j)), 4, i, j)
        return new_matrix

def print_matrix(matrix):
    hash = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            hash += matrix[i][j]
        print hash
        hash = ''


def translate_block(matrix):
    global rules
    return rules[matrix_to_hash(matrix)]

read_rules()

start_matrix = hash_to_matrix('.#./..#/###')

matrix = start_matrix

for i in range(18):
    matrix = expand(matrix)
    print "After " + str(i) + " iterations, " + str(matrix_to_hash(matrix).count('#')) + " pixels are on."



#print_matrix(start_matrix)
#print ''
#print_matrix(expand(start_matrix))
#print ''
#print_matrix(expand(expand(expand(expand(expand(start_matrix))))))
#print matrix_to_hash(expand(expand(expand(expand(expand(start_matrix)))))).count('#')

#print_matrix(hash_to_matrix('#./.#'))
#print_matrix(hash_to_matrix('##./..#/.#.'))
#print ''
#print_matrix(mirror(hash_to_matrix('##./..#/.#.')))
#print ''
#print_matrix(rotate(rotate(hash_to_matrix('##./..#/.#.'))))
#print ''
#print_matrix(rotate(rotate(rotate(hash_to_matrix('##./..#/.#.')))))
#print_matrix(hash_to_matrix('##../...#/..#./####'))


#print rules['#../.#./...']
#print rules['##/##']

#matrix = [['.' for x in range(6)] for y in range(6)]
#matrix[2][2] = '#'
#print matrix
#print get_block(matrix, 2, 1, 1)

#rules = {}

#rules[get_block(matrix, 2, 0, 0)] = get_block(matrix, 2, 1, 1)


#rules['../..'] = get_block(matrix, 2, 1, 1)



# print_matrix(matrix)

# set_block(matrix, translate_block(get_block(matrix, 2, 0, 0)), 2, 0, 0)

# print ''

# print_matrix(matrix)


#print matrix_to_hash(translate_block(get_block(matrix, 2, 0, 0)))
#print matrix_to_hash(get_block(matrix, 2, 1, 1))

