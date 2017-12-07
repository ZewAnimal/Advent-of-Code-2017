
def isValid(l):
    t = set(l)
    if len(l) == len(t):
        return True
    else:
        return False


total = 0
with open("Day4_passphrase_list.txt", "r") as myfile:
    for line in myfile:
        if isValid(line.split()):
            total += 1
    print total

total_v2 = 0
with open("Day4_passphrase_list.txt", "r") as myfile2:
    for phrases in myfile2:
        phrases = phrases.split()
        print phrases.sort()
        #if isValid(phrases.sort()):
            #total_v2 += 1
    print total_v2


#For 2 words to be an anagram they must have the same letters, but in different order.
#This means that if you sum the ASCII values of each letter in a word, they will be equal
#However, there is the possibility that two words may not be anagrams, but they will sum to the
#same value. Must provide a check for this
