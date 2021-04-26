# Program to take a string input and output every second letter in reverse. 
# Weekly Task 03. 
# Author Gerry Donnelly

strin = input("\nEnter a text string: ") # Get the string input.

strout = strin[-1::-2] # The strin is treated as a list. Using -1 to start at the last character and using the -2 step to create the reverse text for every second letter.

print("Input Text :\t{}\nOutput Text:\t{}".format(strin, strout)) # Print the original input text and the reverse output text.

# References used: 
# https://www.w3schools.com/python/python_lists_access.asp