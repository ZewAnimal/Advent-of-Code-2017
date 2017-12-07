
def getMax(num_list):
    temp = 0
    index = 0
    for j in num_list:
        if j > temp:
            temp = j
            index = num_list[j]
    return index


with open("Day6_Memorybank.txt", "r") as myfile:
    mylist = myfile.readline()

max_num = getMax(mylist)
print max_num
