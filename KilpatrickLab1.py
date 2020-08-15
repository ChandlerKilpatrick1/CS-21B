"""
*Program 1 : Lab 1
*Programmer: Chandler Kilpatrick
*Due: 1/14/20
*21 B, Winter 2020
*Description: This program runs a series of equations based the the user input.
""" 

import datetime
today = datetime.date.today()


last_name = input("Please enter your last name: ")

while len(last_name) < 2 or len(last_name) > 15 or last_name.isalpha() == False:
    last_name = input("Please enter your last name: ")

id_number = input("Please enter your ID number: ")

while len(id_number) != 8 or id_number.isdigit() == False:
    id_number = input("Please enter your ID number: ")
    
    

my_id = 0
for item in id_number:
    my_id += int(item)
    
n_let = len(last_name)

print("my_id is : " + str(my_id))
print("n_let is : " + str(n_let))

expression_list = []


expression_one = my_id / 2
expression_list.append(expression_one)
print("expression 1: " + str(expression_list[0]))

expression_two = my_id % 2
expression_list.append(expression_two)
print("expression 2: " + str(expression_list[1]))

expression_three = 0
for i in range(n_let + 1):
    
    if i >= 2:
        expression_three += i
expression_list.append(expression_three)
print("expression 3: " + str(expression_list[2]))

expression_four = my_id + n_let
expression_list.append(expression_four)
print("expression 4: " + str(expression_list[3]))

expression_five = abs(n_let - my_id)
expression_list.append(expression_five)
print("expression 5: " + str(expression_list[4]))

expression_six = (my_id) / (n_let + 1100)
expression_list.append(expression_six)
print("expression 6: " + str(expression_list[5]))

expression_seven = (n_let % n_let) and (my_id * my_id)
expression_list.append(expression_seven)
print("expression 7: " + str(expression_list[6]))

expression_eight = 1 or (my_id / 0)
expression_list.append(expression_eight)
print("expression 8: " + str(expression_list[7]))

expression_nine = round(3.15, 1)
expression_list.append(expression_nine)
print("expression 9: " + str(expression_list[8]))

print("Today's date is " + str(today))


"""                         MY RUNS

##################################################################

======= RESTART: /Users/chandlerkilpatrick/Documents/KilpatrickLab1.py =======
Please enter your last name: Kilpatrick
Please enter your ID number: 20407711
my_id is : 22
n_let is : 10
expression 1: 11.0
expression 2: 0
expression 3: 54
expression 4: 32
expression 5: 12
expression 6: 0.01981981981981982
expression 7: 0
expression 8: 1
expression 9: 3.1
Today's date is 2020-01-14
>>> 

##################################################################



##################################################################
"""







