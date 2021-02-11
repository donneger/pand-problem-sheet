# Program to take positive integer inputs and outputs the successive values of the following calculation.
# 


# Author: Gerry Donnelly

# prepare the variables
numinput = int(input("Please enter a positive number:"))
numout = int() #Will use this for the output. 
numlist = [] # Empty list to be used to hold the numbers for each calculation.

# Take the user input, check if it is a valid integer, i.e. not negative. 
while numinput < 0: # Cannot have a negative number. 
    numinput = int(input("You have entered a negative number, please enter only a positive number:"))

numlist.append(numinput) # Get here when positive integer is input, add it to the list as the first number. 

# Calculation section, as long as the calculation result is not equal to 1 the program checks each succesive result. 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. Append each result to the list
while numout != 1:
    if numinput%2 == 0: # If value is even divide it by 2 and append to the list. 
        numout = int(numinput/2)
        numlist.append(numout)
        numinput = numout
    else:
        numout = int((numinput*3)+1) # if value is odd multiply by 3 and add 1 and add to list. 
        numlist.append(numout)
        numinput = numout

# Get here because the calculation has resulted in 1 so loop ends. 
print (numlist) # Print the resulting list of numbers from the calculation. 