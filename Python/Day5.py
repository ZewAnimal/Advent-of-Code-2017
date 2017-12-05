
def listJumper(mylist):
    steps = 0
    index = 0
    while index < len(mylist):
        jump = mylist[index]
        mylist[index] += 1
        index += jump
        steps += 1
    return steps

with open("Day5_maze.txt", "r") as myfile:
    mylist = [line for line in myfile]

mylist = map(int, mylist)

print listJumper(mylist)



















