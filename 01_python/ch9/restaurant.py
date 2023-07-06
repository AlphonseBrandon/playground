'''
Author: Alphonse Brandon
Date Created: 06-07-2023
Subject: Ch9 - Working with clases
'''
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f'Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

restaurant = Restaurant('TFC', 'Grilled Chicken')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()