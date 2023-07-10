'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''

filename = 'learning_python.txt'

with open(filename) as f:
    content = f.read()
    print(content)