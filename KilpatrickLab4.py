"""
Program 4 : KilpatrickLab4
Programmer: Chandler Kilpatrick
Due: 2/4/20
CS 21 B, Winter 2020
Description: This program changes that way a date is printed. 
""" 

import re
# This regex establishes the format for the dates.
search = "(1[0-2]{1}|0[1-9]{1})/(3[0-1]{1}|[1-2]{1}[0-9]{1}|0[1-9]{1})/([1-2]{1}[0-9]{3})"

# This function will create the formated dates.
def lab_four():

    given_date = input("Please enter a date formatted as shown, mm/dd/yyyy ")

    if re.match(search, given_date):
        pass
    else:
        print("Date input is not valid.")
        raise SystemExit
    
    # This splits the date into day, month, and year.
    month, day, year = given_date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)

    # This is the number of days in each month to compare with.
    number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
    # This is the list of months to compare with. 
    months = ["January", "Febuary", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November,", "December"]

    # This determines if the given date is a leap year.
    if day == 29 and month == 2:
        if ((year % 4 == 0 and year % 100 != 0) or year % 4 == 0) == False:
            print("Date input is not valid.")
            raise SystemExit

    elif day >= number_of_days[month -1]:
        print("Date input is not valid.")
        raise SystemExit
    
    # This prints the converted date.
    print("The converted date is: "+months[month - 1]+" "+str(day)+", "+str(year))

# CONSTANT
NUM_DATES = 5

x = 0
# This loops through the code 5 times. 
while x <= NUM_DATES:
    lab_four()
    x += 1


"""                         MY RUNS

##################################################################

/Users/chandlerkilpatrick/Desktop/CS21B/KilpatrickLab4.py 
Please enter a date formatted as shown, mm/dd/yyyy 10/30/2530
The converted date is: October 30, 2530
Please enter a date formatted as shown, mm/dd/yyyy 07/27/1852
The converted date is: July 27, 1852
Please enter a date formatted as shown, mm/dd/yyyy 12/12/1212
The converted date is: December 12, 1212
Please enter a date formatted as shown, mm/dd/yyyy 02/29/2020
The converted date is: Febuary 29, 2020
Please enter a date formatted as shown, mm/dd/yyyy 02/29/2021
Date input is not valid.
(base) bash-3.2$ 

##################################################################



##################################################################
"""

