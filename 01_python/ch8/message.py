'''
Author: Alphonse Brandon
Date Created: 04-07-2023
Subject: Ch6 - Working functions
'''

def display_message():
    print('Hi, I am currently learning Python!')

display_message()

def favourite_book(book):
    print(f'One of my favourite books is {book}')
favourite_book('The Power of your Mind')

def make_shirt(text='I love Python',size='large'):
    print(f'The size of the shirt is {size} and you want the following message printed on it: \n"{text}"')


message = 'Education is a powerful weapon'

make_shirt()
