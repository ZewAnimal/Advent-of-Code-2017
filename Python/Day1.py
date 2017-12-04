
with open("Day1_number_list.txt", "r") as myFile:
    temp = [j for i in myFile for j in i]

sum = int(temp[0])
size = len(temp) - 1
for i, j in enumerate(temp):
    if (i+1 <= size):
        if j == temp[i+1]:
            sum = sum + int(j)

print sum

#Answer = 1031