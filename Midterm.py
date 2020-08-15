"""import re

test1 = "This is a test"

test2 = "A test this is"
test3 = "1st test this is"
test4 = "66"
test5 = "This is test 1 not 2"

if re.match("[Tt]his", test1):            # regex1
   print("This or this")
else:
   print("no match")

if re.match("^This|this", test2):         # regex2
   print("A test this is")
else:
   print("no match")

if re.match(r'^\d\d$', test3):            # regex3
    print('A match test3')
elif re.match(r'^\d\d$', test4):
    print('A match test4')
elif re.match(r'^\d\d$', test5):
    print('A match test 5')
"""
'''
a = [ 2, 3, 5, 7, 8, 10]
result= list(filter(lambda x: not (x % 2), a))
print(result)
'''
'''
from datetime import datetime

MM = 5
DD = 14
YYYY = 2018

date_obj = datetime.date(YYYY, MM, DD)
date_str = date_obj.strftime('%m/%d/%y')
print(date_str)
'''
'''
test = "today is Tuesday"
asplit = test.split()
print(type(asplit))
'''
'''
import functools 

f = lambda x, y: x + y
result = functools.reduce(f, range(2,5)) 
print(result)
'''
'''
first_list = [1,2,3]
second_list = first_list * 2
print(second_list)
'''
import re

# content = 'In a land far far away called never land'
# def frequency(content):
#     pattern = '[a-zA-Z]+'
#     words = re.findall(pattern, content)
#     dictionary = {}
#     for w in words:
#         if w in dictionary:
#             dictionary[w] += 1
#         else:
#             dictionary[w] = 1
#     return dictionary

# print(frequency(content))
# print(re.findall('ca*t', 'ct, cat, castle, cartwheel'))
'''

members = ["555-2345 Foothill, Ann",
           "DeAnza, P. Bob",
           "552-4301 Fish, Mardy",
           "555-7666 Smith, Claire May"]
for i in members:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)",i)
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))
    '''
import re
print(re.findall("\d\d","365 days in '18, Oh My!"))

