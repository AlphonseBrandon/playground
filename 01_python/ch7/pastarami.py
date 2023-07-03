'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working with while loops
'''

food_menu = ['eru', 'rice', 'beans', 'yam', 'rice', 'salad', 'rice']

print('The restaurant has run out of rice\n')

delivered_food = []

while 'rice' in food_menu:
    food_menu.remove('rice')
while food_menu:
    ordered_food = food_menu.pop()
    print(f'Currently making {ordered_food}')
    delivered_food.append(ordered_food)
print('\n--Delivered Food--')
for food in delivered_food:
    print(food)