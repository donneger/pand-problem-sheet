# Program to count the number of "e" letters in a text file. 
# This program uses the text of the novel Moby Dick. 
# The text for counting uses the novel text only, excludes the file intro and etymology.

# Author: Gerry Donnelly

import sys # Module to allow arguments / variables to be used in the python runtime environment.

with open(sys.argv[1], "r") as filetext: # Open the file entered on the command line, in this case MobyDick.txt.
    readfile = filetext.read()  # Read in the text
    filelen = (len(readfile)) # Calculate the total length of the text. 
    ecount = readfile.count('e') # Count the number of 'e' characters in the text
    
    # Print out the results. Using {:,} to format the numbers output.
    print("\nThe total numbers of characters (letters) in the text is: {:,}\nThe total count for the letter 'e' is {:,}\n".format(filelen, ecount))

    # References:
    # https://www.gutenberg.org/files/2701/old/moby10b.txt. This is tthe source of the text I used. 
    # https://www.tutorialsteacher.com/python/sys-module

