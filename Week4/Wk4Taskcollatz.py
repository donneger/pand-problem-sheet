# Program to take positive integer inputs and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author: Gerry Donnelly

numinput = int(input("Please enter a positive number:"))
numout = int()
numlist = []
while numinput < 0:
    numinput = int(input("You have entered a negative number, please enter only a positive number:"))

while numout != 1:
    if numinput%2 == 0:
        numout = numinput/2
        numlist.append(numout)
    else:
        numout = (numinput*3)+1
        numlist.append(numout)

print (numlist)