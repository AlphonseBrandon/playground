'''
Author: Alphonse Brandon
Date Created: 28-06-2023
Subject: Conditional test with if statements
'''

alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You just earned 15 points!')

# Stages of life

age = 91

if age < 2:
    print('You are a baby')
elif age < 4:
    print('You are a toddler')
elif age < 13:
    print('You are a kid')
elif age < 20:
    print('You are a teenager')
elif age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')

# Favorite fruit

fruits = ['apple', 'banana', 'orange', 'grape', 'watermelon']

favourite_fruits = fruits[:3]

if 'apple' in favourite_fruits:
    print('You really like apples!')
if 'banana' in favourite_fruits:
    print('You really like bananas!')
if 'orange' in favourite_fruits:
    print('You really like oranges!')
if 'grape' in favourite_fruits:
    print('You really like grapes!')
if 'watermelon' in favourite_fruits:
    print('You really like watermelons!')