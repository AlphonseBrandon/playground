'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch9 - Working with built in python modules
'''

import random
count = 0
possibilities = ['a', 2, 'b', 4, 'e', 'f']
my_response= 'a'
win = random.choice(possibilities)

while my_response != win:
    win = random.choice(possibilities)
    count += 1
    if my_response == win:
        break

print(f'It took {count} try to get to the correct result')
