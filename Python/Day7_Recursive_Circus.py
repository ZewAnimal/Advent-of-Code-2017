import re

#Part 1
def get_name_of_root(namelist, childlist):
    for name in namelist:
        flag = True
        for child in childlist:
            if name in child:
                flag = False
                break
        if flag == True:
            return name
    return None


mylist =[]
with open("Day7_input.txt", "r") as myfile:
    for line in myfile:
        mydict = {}
        split_line = line.split()
        if "->" in line:
            mydict['name'] = split_line[0]
            mydict['weight'] = split_line[1]
            mydict['children'] = split_line[3:]
            mylist.append(mydict)
        else:
            mydict['name'] = split_line[0]
            mydict['weight'] = split_line[1]
            mydict['children'] = None
            mylist.append(mydict)

#create a list of names that are roots, and a list of children that are not leaves
name_list = [i['name'] for i in mylist if i['children'] is not None]
child_list = [i['children'] for i in mylist if i['children'] is not None]

#remove extra comma from end of second element
child_list = [x.strip(',') for i in child_list for x in i]

for item in mylist:
    x = item['weight']
    y = re.search('(\d+)', x)
    item['weight'] = int(y.group())


root = get_name_of_root(name_list, child_list)
print root
for i in mylist:
    if i['children'] is None:




