'''
Author: Alphonse Brandon
Date Created: 22-06-2023
Subject: slicing and list copying
'''

foods = ['beans', 'yam', 'rice', 'meat', 'banana']

message = 'Elements in the list are:'
print(message)
for food in foods:
    print(food)

message1 = 'The first three elements in the list are:'

print(message1)
for food in foods[:3]:
    print(food)

message2 = 'Two items from the middle are:'

print(message2)
for food in foods[2:4]:
    print(food)

message3 = 'The last three elements are:'

print(message3)
for food in foods[-3:]:
    print(food)

alphonse_foods = foods[:]
alphonse_foods.append('koki')

message4 = 'Elements in orginal food:'
print(message4)

for food in foods:
    print(food)

message5 = 'Elements in Alphonse Fooda:'

print(message5)
for food in alphonse_foods:
    print(food)

print('Length of foods:')
print(len(foods))

print('Length of Alphonse foods')
print(len(alphonse_foods))