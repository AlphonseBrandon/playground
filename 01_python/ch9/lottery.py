'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch9 - Working with clases and intances of classes
'''

import random

odds = ['a', 'c', 1, 'e', 5]
win = random.choices(odds, k=4)

print(f'If you selected this four combination {win}, then you won the lottery')
