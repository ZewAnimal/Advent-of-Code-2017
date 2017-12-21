import csv
from itertools import cycle


def spin_to_win(n, mylist):
    return mylist[-n:] + mylist[:-n]

def exchange_yo_partner_by_index(a, b, mylist):
    mylist[a], mylist[b] = mylist[b], mylist[a]
    return mylist

def exchange_yo_partner_by_name(a, b, mylist):
    i = mylist.index(a)
    j = mylist.index(b)
    mylist[i], mylist[j] = mylist[j], mylist[i]
    return mylist

programs = [str(unichr(i)) for i in range(97, 113)]

with open('Day16_dance_moves.csv', 'r') as myfile:
    dance_moves = csv.reader(myfile)
    k = 0
    #while k < 1000000000:
    for move in dance_moves:
        print move
        for i in move:
            if i[0] == 's':
                programs = spin_to_win(int(i[1:]), programs)
                k += 1
            elif i[0] == 'x':
                temp = i[1:].split('/')
                exchange_yo_partner_by_index(int(temp[0]), int(temp[1]), programs)
                k += 1
            else:
                temp = i[1:].split('/')
                exchange_yo_partner_by_name(temp[0], temp[1], programs)
                k += 1

