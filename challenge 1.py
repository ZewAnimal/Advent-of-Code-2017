#from string import maketrans


myString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle " \
           "gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq " \
           "pcamkkclbcb. lmu ynnjw ml rfc spj"

mylist = [sum(bytearray(i)) for i in myString]
print mylist
for index, num in enumerate(mylist):
    if mylist[index] > 96 and mylist[index] < 121:
        mylist[index] = num + 2
    elif mylist[index] == 121:
        mylist[index] = 97
    elif mylist[index] == 122:
        mylist[index] = 98
    else:
        pass

mylist = [str(unichr(x)) for x in mylist]
mystr = ''.join(mylist)
print mystr
