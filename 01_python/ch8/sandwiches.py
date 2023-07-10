'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

person1_food = ['meat', 'fish', 'rice']

person2_food = ['eru', 'fufu']

def sandwiches(*foods: list) -> None:
    """Print a summary of the food ordered"""
    print("You ordered the following foods:")
    for food in foods:
        print(food)

sandwiches(person1_food)
sandwiches(person2_food)