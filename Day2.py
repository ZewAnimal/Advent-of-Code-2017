
with open("Day2_spreadsheet.txt", "r") as myfile:
    mylist = [line.split() for line in myfile]

sum = 0
for i in mylist:
    i = map(int, i)             #convert list of str to int
    sum = sum + (max(i) - min(i))

print sum