# Program to calculate BMI for pands Lab 2.2
# Author: Gerry Donnelly
# Program takes Height and Weight inputs from the user and outputs the BMI score and indicates if Low, Normal or High

class color: # Define Class color to help with formatting the output strings, sourced from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python/8930747
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

format = color() 

# Inputs are converted to integers at the input stage by adding "int(.....")
Height = int(input("Please enter your " + format.BOLD + format.UNDERLINE + "Height" + format.END + " in CM: ")) # User inputs Height in CM"
Weight = int(input("Please enter your " + format.BOLD + format.UNDERLINE + "Weight" + format.END + "in KG: ")) # User inputs Weight in KG"

BMI = Weight/((Height/100)*2)   # Calculate the BMI from the user inputs.

# This section checks the BMI result against the normal BMI ctriteria for Low, Normal, High and prints out the result, text is formatted based on the result. 
if BMI<18.5:    # Check if BMI low
    print ("Your BMI is " + format.RED + format.BOLD + format.UNDERLINE + str(BMI) + " and is LOW" + format.END)
elif BMI>25:    #Check if BMI is High
        print ("Your BMI is " +  format.RED + format.BOLD + format.UNDERLINE+ str(BMI) + " and is HIGH" + format.END) 
else:   # If BMI is not Low or High then it is Nornal.
    print ("Congrats Your BMI is " + format.GREEN + format.BOLD + format.UNDERLINE + str(BMI)  + " and is NORMAL " + format.END) # If not Low or High then it is Nornal.