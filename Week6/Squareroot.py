# Program to calculate Square Root using Newtons Method.
# Author: Gerry Donnelly

# This method uses successive iterations of the formula: root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
# A desired accuracy level the user can input is also included, the output is rounded to 4 decimal places. 
# Source https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/



# The sqroot function provides the calculation of the numnber to be rooted. The number and the accuracy level are passed in from the program. 
#The other variables used are initialised in the arguments as 1 and 0. 
def sqroot (number, accuracy, test = 1, root= 0):
    
    guess = number #first guess is number to be rooted. 
    while test > accuracy: # Keep calculating until desired accuracy level is reached.
        root = (guess + number/guess)/2 # This is the formula used for the calculation, it is repeated until desired accuracy is reached. 
        test = abs(root - guess)
        if test < accuracy:
            return root
        guess = root 

# User inputs for the number to be rooted and accuracy level required as thi is an approximation formula. 
number = int(input("Please input the number to be rooted:"))
t = float(input("Please enter the accuracy level desired in %, e.g. 99.999: "))

# Convert the accuracy for use in the functions
accuracy = 1-(t/100)

# The sqroot function is called from the print function and the "root" value is returned and printed out. 
print ("The number input was: {}. The Square Root of the number is {}".format(number, round(sqroot(number, accuracy),4)))
