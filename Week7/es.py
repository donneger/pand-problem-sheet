# Program to count the number of "e" characters in a text file. 
# This program uses the text of the noverl Moby Dick , source https://www.gutenberg.org/files/2701/old/moby10b.txt
# The text for counting uses the novel text only, excludes the file intro and etymology.

# Author: Gerry Donnelly

filename = ('MobyDick.txt') 

with open(filename, "r") as filetext: # Open the file for reading. 
    readfile = filetext.read()  # Read in the text
    filelen = (len(readfile)) # Calculate the total length of the text. 
    ecount = readfile.count('e') # Count the number of 'e' characters in the text
    
    # Print out the results. Using {:,} to format the numbers output.
    print("The total numbers of characters (letters) in the text is: {:,}\nThe total count for the letter 'e' is {:,}".format(filelen, ecount))