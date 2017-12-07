
#Part 1
def listJumper(mylist):
    steps = 0
    index = 0
    while index < len(mylist):
        jump = mylist[index]
        mylist[index] += 1
        index += jump
        steps += 1
    return steps

#Part 2
def listJumper_v2(mylist):
    steps = 0
    index = 0
    while index < len(mylist):
        jump = mylist[index]
        if jump >= 3:
            mylist[index] -= 1
        else:
            mylist[index] += 1
        index += jump
        steps += 1
    return steps

with open("Day5_maze.txt", "r") as myfile:
    mylist = [line for line in myfile]

mylist = map(int, mylist)
mylist_v2 = list(mylist)

print "Answer to #1 = {}" \
      "\nAnswer to #2 = {}"\
    .format(listJumper(mylist), listJumper_v2(mylist_v2))
















