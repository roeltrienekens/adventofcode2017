inputfile = "input.txt"
testfile = "input_test.txt"

tree = {}       # dict with list of children per node
values = {}     # weight of all nodes
frequency = {}  # amount of occurences (root node is only one with freq 1)

def parse_tree(inputfile):
    f = open(inputfile, 'r')
    for line in f:
        ops = line.split()
        target = ops[0]
        inc_frequency(target)
        height = int(ops[1].replace("(", "").replace(")", ""))
        values[target] = height
        children = []
        while len(ops) > 3:     # TODO make list comprehension
            print(ops)
            child = ops.pop().replace(",", "")
            inc_frequency(child)
            children.append(child)
            print(children)
            tree[target] = children


    print(tree)

def inc_frequency(key):
    if frequency.has_key(key):
        frequency[key] += 1
    else:
        frequency[key] = 1

def find_root():
    for name, freq in frequency.iteritems():
        if int(freq) == 1:
            return name

def get_weight(node):
    weight = values[node]
    if tree.has_key(node):
        for child in tree[node]:
            weight += get_weight(child)
    return weight

def is_balanced(node):
    if tree.has_key(node):
        weight = -1
        for child in tree[node]:
            if weight == -1:
                weight = get_weight(child)
            if get_weight(child) != weight:
                return False
    return True

def find_unbalanced_node(node):
    if tree.has_key(node):
        for child in tree[node]:
            if not(is_balanced(child)):
                return find_unbalanced_node(child)
        return node
    return node

if __name__ == '__main__':

    parse_tree(inputfile)
    print("The root is " + find_root())
    print("The root has weight " + str(get_weight(find_root())))
    unbalanced_node = find_unbalanced_node(find_root())
    print("The unbalanced node is " + unbalanced_node)
    print(is_balanced(unbalanced_node))

    # We now have the deepest unbalanced node, so one of the children should be changed.

    for child in tree[unbalanced_node]:
        print("Node weight of " + child + " is " + str(get_weight(child)))

