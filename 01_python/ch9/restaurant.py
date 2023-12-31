'''
Author: Alphonse Brandon
Date Created: 06-07-2023
Subject: Ch9 - Working with clases and intances of classes
'''
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> None:
        print(f'Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')
    
    def set_number_served(self, number: int) -> None:
        """"Set the number served"""
        self.number_served = number

    def increment_number_served(self, increment: int) -> None:
        """Increments the number served"""
        self.number_served += increment

restaurant1 = Restaurant('TFC', 'Grilled Chicken')
restaurant2 = Restaurant('48 Spices', 'Grilled Chicken and Plantains')
restaurant3 = Restaurant('J and J', 'Eru and Garri')


restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant1.set_number_served(10)

restaurant1.increment_number_served(5)

print(f'Number of restaurant served {restaurant1.number_served}')