"""
Program 5 : KilpatrickLab5
Programmer: Chandler Kilpatrick
Due: 2/18/20
CS 21 B, Winter 2020
Description: This program will print the number of occurences of specified topics
""" 

import datetime 
from urllib.request import urlopen
import re

# This function runs the program.
def calculate():
    topics = ['research', 'climate', 'evolution', 'cultural', 'leadership', 'nation', 
    'physical', 'science', 'biological', 'membership']
    topic_count = dict()

    # This prints the current date.
    print(f"Today's date is {datetime.date.today()}")

    # These lines opena nd decode the website. 
    url = 'http://www.nasonline.org/'
    response = urlopen(url)
    html = response.read()
    decoded_html = html.decode()

    # This for loop will find the the number of times each topic is mentioned. 
    for topic in topics:
        regex = '(?:^|\W)' + topic + '(?:$|\W)'
        a = re.findall(str(regex), decoded_html, re.IGNORECASE)
        topic_count[topic] = len(a)

    # This for loop will print the correct format.
    for k,v in topic_count.items():
        print(f"{k} appears {v} times.")

calculate()
 
"""                         MY RUNS

##################################################################

/Users/chandlerkilpatrick/Desktop/CS21B/KilpatrickLab5.py 
Today's date is 2020-02-18
research appears 9 times.
climate appears 3 times.
evolution appears 4 times.
cultural appears 8 times.
leadership appears 4 times.
nation appears 1 times.
physical appears 1 times.
science appears 26 times.
biological appears 1 times.
membership appears 11 times.
(base) bash-3.2$ 

##################################################################



##################################################################
"""



