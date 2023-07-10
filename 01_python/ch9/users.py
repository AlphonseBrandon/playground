'''
Author: Alphonse Brandon
Date Created: 06-07-2023
Subject: Ch9 - Working with clases mimicking real word objects
'''

class Users:
    def __init__(self, first_name: str, last_name: str, location: str):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.login_attempt = 0

    def describe_user(self) -> None:
        '''Display user information'''

        print("User Information:\n")
        print(f'\tFirst Name: {self.first_name}\n\tLast name: {self.last_name}\n\tLocation: {self.location}')
    
    def greet_user(self) -> None:
        '''Display personalize greeting to user'''

        print(f'\nHello {self.first_name} how is the weather in {self.location} today')

    def increment_login_attempt(self) -> None:
        """Increments the login attempt by 1"""
        self.login_attempt += 1

    def reset_login_attempts(self) -> None:
        """Reset the login attempt to 0"""
        self.login_attempt = 0

user1 = Users('Alphonse', 'Brandon', 'Buea')

user1.describe_user()
user1.greet_user()

user1.increment_login_attempt()
user1.increment_login_attempt()
print(f'Login attempts: {user1.login_attempt}')

user1.reset_login_attempts()
print(f'Login attempts Reset to: {user1.login_attempt}')