
with open("Day2_spreadsheet.txt", "r") as myfile:
    mylist = [line.split() for line in myfile]

#Part 1
sum = 0
for i in mylist:
    i = map(int, i)             #convert list of str to int
    sum = sum + (max(i) - min(i))

print sum

#Part 2
sum_v2 = 0
for i in mylist:
    i = map(int, i)
    for j, k in enumerate(i):
        while j < len(i) - 1:
            if k > i[j+1] and k % i[j+1] == 0:
                sum_v2 += k/i[j+1]
                j += 1
            elif i[j+1] % k == 0:
                sum_v2 += i[j+1]/k
                j += 1
            else:
                j += 1

print sum_v2




