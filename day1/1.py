myfile = open(r"in1a.txt")

mylist = []

c = myfile.read(1)
while c != "\n":
    mylist.append(c)
    c = myfile.read(1)
    print(c)

print(mylist)

captchaSum = 0
listLength = len(mylist)
offset = len(mylist) / 2

for i in range(0, len(mylist)):
#    print mylist[i]
#    print mylist[(i + offset) % listLength]
    if mylist[i] == mylist[(i + offset) % listLength]:
        captchaSum += int(mylist[i])

# if mylist[0] == mylist[len(mylist) - 1]:
#    captchaSum += int(mylist[0])

print(captchaSum)

#
