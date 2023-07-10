'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch9 - Working with clases and intances of classes
'''

import users as us

class Admin(us.Users):
    def __init__(self, first_name: str, last_name: str, location: str):
        super().__init__(first_name, last_name, location)
        self.privileges = Privileges()

    

class Privileges:
    def __init__(self) -> None:
        self.privileges = ['can post', 'can delete', 'can ban user']

    def show_privileges(self) -> None:
        """List the privileges of the user"""
        print(self.privileges)


user2 = Admin('Alphonse', 'Brandon', 'Buea')

user2.privileges.show_privileges()
