'''
Author: Alphonse Brandon
Date Created: 28-06-2023
Subject: Combining multiple conditions
'''

usernames = ['admin', 'brandon', 'james', 'jessica', 'jennifer']

for username in usernames:
    if username is 'admin':
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

new_users = ['admin', 'Brandon', 'james', 'jessica', 'jennifer', 'joseph']

for new_user in new_users:
    if new_user in current_users:
        print(f'The username {new_user} has already been used')
    else:
        print(f'The username {new_user} is available') 

# Ordinal numbers 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers[:4]:
    if number is numbers[0]:
        print(f'{number}st')
    if number is numbers[1]:
        print(f'{number}nd')
    if number is numbers[2]:
        print(f'{number}rd')
for number in numbers[3:]:
    print(f'{number}th')