'''
Author: Alphonse Brandon
Date Created: 30-06-2023
Subject: Working with dictionaries
'''
favourite_languages = {
    'jen' : 'python',
    'romeo' : 'javascript',
    'joseph' : 'c',
    'ann' : 'ruby',
}

take_the_poll = ['jen', 'romeo', 'alphonse', 'brandon']

for name in take_the_poll:
    if name in favourite_languages.keys():
        print(f'Thank you for taking the poll {name}\n')
    if name not in favourite_languages.keys():
        print(f'Hi {name} please take the poll\n')