from itertools import cycle

with open("Day1_number_list.txt", "r") as myFile:
    temp = [j for i in myFile for j in i]

#Part 1
sum = int(temp[0])
size = len(temp) - 1
for i, j in enumerate(temp):
    if (i+1 <= size):
        if j == temp[i+1]:
            sum += int(j)

print sum
#Answer = 1031

step = size/2



'''#Part 2
steps = (len(temp)-1)/2
print steps
mylist = cycle(temp)
sum_v2 = 0
for i, j in enumerate(mylist):
    if i == size:
        break
    if j == temp[i + steps]:
        sum_v2 += (int(j) * 2)

print sum_v2'''