'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''

filename  = 'guest_book.txt'
print('Enter q to quit')


while True:
    name = input('Enter your name: ')
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f'{name}\n')
    