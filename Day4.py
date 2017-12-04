
def isValid(list):
    t = set(list)
    if len(list) == len(t):
        return True
    else:
        return False

total = 0
with open("Day4_passphrase_list.txt", "r") as myfile:
    for line in myfile:
        if (isValid(line.split()) == True):
            total += 1
        else:
            pass

print total
