import math

givenInput = 312051
    #get the size of the matrix based on given input
    #559 x 559 Matrix with '1' at the center

root = math.sqrt(givenInput)
root = math.ceil(root)

se_diagonal = root*root

print se_diagonal - givenInput


#312051 < 559^2, so it will be to the left of the SE corner of the grid
#by 430 spaces (559^2 - 312051)
#Answer = 430 spaces

#Part 2


x = y = 0
z = 1
grid = []
total = 0

while total <= givenInput:








