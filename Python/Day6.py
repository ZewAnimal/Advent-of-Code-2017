import unittest


def memory_bank_mover(banklist):
    max_num = max(banklist)
    start_index = banklist.index(max_num)
    banklist[start_index] = 0
    for i in range(1, max_num+1):
        banklist[(start_index + i) % len(banklist)] += 1
    return banklist

def check_for_duplicates(banklist):
    t = set(banklist)
    if len(t) != len(banklist):
        return True
    else:
        return False

with open("Day6_Memorybank.txt", "r") as myfile:
    mylist = [map(int, i.split()) for i in myfile if i.strip()]

temp = list(mylist)
new_bank = memory_bank_mover(temp[0])
mylist.append(new_bank)
print mylist




class TestThatBank(unittest.TestCase):

    def test_memory_bank_mover(self):
        self.assertEqual([1,2,3,0], memory_bank_mover([0,1,2,3]))


if __name__ == '__main__':
    unittest.main()