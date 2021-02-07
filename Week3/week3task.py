# Program to take a string input and output every second letter in reverse. 
#Author Gerry Donnelly

strin = input("Enter a text string: ") # Get the string input.

strout = strin[-1::-2] # Using -1 to start at the last character and using the -2 step to create the reverse text for every second letter.

print("Input Text :\t{}\nOutput Text:\t{}".format(strin, strout)) # Print the original input text and the reverse output text.