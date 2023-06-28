'''
Author: Alphonse Brandon
Date Created: 28-06-2023
Subject: Combining multiple conditions
'''

usernames = ['admin', 'brandon', 'james', 'jessica', 'jennifer']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again')
no_users = []

# check if list is empty
if no_users:
    for no_user in no_users:
        print(f'Hello {no_user}, thank you for logging in again')
else:
    print('We need to find some users!')

current_users = ['admin', 'brandon', 'james', 'jessica', 'jennifer']

new_users = ['admin', 'brandon', 'james', 'jessica', 'jennifer', 'joseph']

for new_user in new_users:
    if new_user in current_users:
        print(f'The username {new_user} has already been used')
    else:
        print(f'The username {new_user} is available') 