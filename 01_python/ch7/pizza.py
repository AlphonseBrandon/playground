'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working with while loops
'''

prompt = '\nEnter the list of food you which to eat '

prompt += "\nEnter 'quit' to end the program\n"

active = True

while active:
    food = input(prompt)
    if food == 'quit':
        active = False
    if food:
        print(f'We will add {food.title()} to your list')
