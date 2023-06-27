'''
Author: Alphonse Brandon
Date Created: 27-06-2023
Subject: Conditional test with if statements
'''

car = 'subaru'

print("is car == 'subaru'? I predict True.")

print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car=='audi')

age = 19

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}')