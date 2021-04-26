# Program to take positive integer inputs, and outputs the successive values of the following calculation.
# if the number divided by 2 is even, divide it by two, but if it is odd, multiply it by three and add one. Append each result to the list


# Author: Gerry Donnelly

# prepare the variables
numinput1 = int(input("\nPlease enter a positive number: "))
numinput2 = numinput1 # Use this to hold the original input number, will use in the final printout. 
numout = int() # Will use this for the output. 
numlist = [] # Empty list to be used to hold the numbers for each calculation.

# Take the user input, check if it is a valid integer, i.e. not negative. 
while numinput1 < 0: # Check if negaive number entered. 
    numinput1 = int(input("You have entered a negative number, please enter only a positive number:"))
    numinput2 = numinput1 # Will use this for the output.
numlist.append(numinput1) # Get here when positive integer is input, add it to the list as the first number. 

# Calculation section, as long as the calculation result of the number to be output is not equal to 1 the program checks each succesive result. 
# if the number divided by 2 is even, divide it by two, but if it is odd, multiply it by three and add one. Append each result to the list
while numout != 1:
    if numinput1%2 == 0: # If value is even divide it by 2 and append to the list. 
        numout = int(numinput1/2)
        numlist.append(numout)
        numinput1 = numout
    else:
        numout = int((numinput1*3)+1) # if value is odd multiply by 3 and add 1 and add to list. 
        numlist.append(numout)
        numinput1 = numout

# Get here because the calculation of "numout" has resulted in 1 so loop ends. 
print ("The number you entered was {}, the resulting output from the calculation is: \n" .format(numinput2)) # Print the resulting list of numbers from the calculation. 
print(numlist,"\n")


#References:
# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_conditions.asp
