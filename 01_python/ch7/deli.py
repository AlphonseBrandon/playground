'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working with while loops
'''

food_menu = ['eru', 'rice', 'beans', 'yam']

delivered_food = []

while food_menu:
    ordered_food = food_menu.pop()
    print(f'I made your {ordered_food}')
    delivered_food.append(ordered_food)
print('---Food Delivered--')
for food in delivered_food:
    print(food)