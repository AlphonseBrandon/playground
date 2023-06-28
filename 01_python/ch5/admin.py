'''
Author: Alphonse Brandon
Date Created: 28-06-2023
Subject: Combining multiple conditions
'''

usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again')
