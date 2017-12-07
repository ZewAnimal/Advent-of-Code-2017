
ok = True
ll = [0, 2, 3, 4, 5]
print len(ll)

while ok:
    print("Enter two words and I will tell you if they're anagrams, bitch. ")
    a = raw_input("\nFirst word:    ")
    b = raw_input("Second word:    ")

    byte_a = sum(bytearray(a))
    byte_b = sum(bytearray(b))

    if byte_a == byte_b:
        print "\nYes! {} and {} are anagrams, bitch!".format(a, b)
    else:
        print "\nNot an anagram, bitch."

    c = raw_input("\nHow about another go, bitch? [y/n]")
    if c == 'n':
        ok = False
