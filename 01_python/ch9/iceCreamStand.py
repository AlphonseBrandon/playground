'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch9 - Working with clases and intances of classes
'''

import restaurant as rt

class IceCreamStand(rt.Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:    
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'milk', 'egg']

    def flavourss(self) -> None:
        """Print the list of flavours""" 
        
        print(self.flavours)

first = IceCreamStand('IYA', 'African')

first.flavourss()