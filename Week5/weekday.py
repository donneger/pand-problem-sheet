# Program to indicate if current date is a weekday.

# Author: Gerry Donnelly.

import datetime as dt # Import datetime module to convert system time.

today = dt.datetime.now().strftime("%A") # Get todays date and format it to get full day name in string format. 

#today = "Sunday" 

# Set up days of week, day and day type. 
daysofweek = {
    "Monday" : "Weekday",
    "Tuesday" : "Weekday",
    "Wednesday" : "Weekday",
    "Thursday" : "Weekday",
    "Friday" : "Weekday",
    "Saturday" : "Weekend",
    "Sunday" : "Weekend",
}

for day, type in daysofweek.items(): # Loop thorugh the dictionary to get the days key and day type.
    if day == today:                   # Check if days key matches what day it is.
        if type == "Weekday":           # When we get a match check the type of day. 
            print ("Today is: {}, unfortunately it is a {}.".format(day, type))     # Get here if it is a weekday. 
            break    # If it is a weekday can break here, no need to go any further. 
        print ("Today is: {}, waahay it is a {}.".format(day, type))    # If it is not a weekday it must be a weekend day. 
        

