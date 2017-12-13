inputfile = "input.txt"

village_map = {}
seen = set()

def init_map():
    for line in open(inputfile, 'r'):
        op1 = int(line.split()[0])
        op2 = list(line.replace(',','').split()[2:])
        village_map[op1] = op2

def get_count(node):
    if node in seen:
        return 0
    else:
        seen.add(node)
        count = 1
        for connected_node in village_map[node]:
            if int(connected_node) not in seen:
                count += get_count(int(connected_node))
        return count

init_map()

print("process 0 is connected to " + str(get_count(0)) + " other processes.")

group_count = 1                 # compensate for the get_count we did above since we mark nodes as seen once we start calling get_count
for i in range(0, 2000):
    cnt = get_count(i)
    if cnt > 0:                 # if part of an existing group, it is connected to 0 *unseen* nodes
        group_count += 1

print("In total there are " + str(group_count) + " separate groups of processes.")

