'''
Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''

print("Enter 'q' to quit")
filename = 'poll.txt'
while True:
    reason = input('Why do you like programming?\n')
    if reason == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f'{reason}\n')
