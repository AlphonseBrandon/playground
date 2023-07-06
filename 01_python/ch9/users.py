'''
Author: Alphonse Brandon
Date Created: 06-07-2023
Subject: Ch9 - Working with clases
'''

class Users:
    def __init__(self, first_name: str, last_name: str, location: str):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def describe_user(self) -> None:
        '''Display user information'''

        print("User Information:")
        print(f'\tFirst Name: {self.first_name}\n\tLast name: {self.last_name}\n\tLocation: {self.last_name}')
    
    def greet_user(self) -> None:
        '''Display personalize greeting to user'''

        print(f'Hello {self.first_name} how is the weather in {self.location} today')
user1 = Users('Alphonse', 'Brandon', 'Buea')

user1.describe_user()
user1.greet_user()
    