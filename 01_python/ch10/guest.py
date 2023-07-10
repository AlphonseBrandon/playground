'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''
name = input('What is your name?\n')

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)