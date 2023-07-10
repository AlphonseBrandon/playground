'''
Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''
import json

fav_number = input('What is your favourite number? ')
filename = 'fav.json'

def store_num():
    with open(filename, 'w') as f:
        json.dump(fav_number, f)

def display_num():
    with open(filename) as f:
        fav_num = json.load(f)
        print(f'I know your favourite number. it is: {fav_num}')

# with open(filename) as f:
#     content = json.load(f)
#     if fav_number == content:
#         display_num()
#     else:
#         store_num()
if filename:
    display_num()
else:
    store_num()
    # display_num()