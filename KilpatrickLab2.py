"""
Program 2 : Lab 2
Programmer: Chandler Kilpatrick
Due: 1/21/20
21 B, Winter 2020
Description: This program determines if a file has valid data and then returns the sum.
""" 
def a():
    file = input("Please enter the file name: ")
    try:
        open_file = open(file, "r")
    except:
        print("Error: file not found.")
        return

    my_list = []

    i = 0
    for line in open_file:

        if i == 0:
            if line.strip().isdigit() == False:
                print("Error: File contents invalid ")
                return
            else:
                num_digits = int(line) 
        else:
            my_list.append(line)
        i = i + 1

    if num_digits != len(my_list):
        print("Error: File contents invalid ")
        return
    
    sumh = 0
    for item in my_list:
        sumh += int(item)
    print("The sum is: " + str(sumh))
  
    open_file.close()

a()

"""                         MY RUNS

##################################################################

Not asked for.

##################################################################



##################################################################
"""
