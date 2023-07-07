'''
Author: Alphonse Brandon
Date Created: 06-07-2023
Subject: Ch9 - Working with Files and exceptions
'''

with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())
    print(f'Lenght of digits {len(content)}')