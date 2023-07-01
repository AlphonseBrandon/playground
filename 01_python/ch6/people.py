'''
Author: Alphonse Brandon
Date Created: 01-07-2023
Subject: Ch6 - Working with dictionaries
'''

person_one = {
    'first_name' : 'alphonse',
    'last_name' : 'brandon',
    'age' : 30,
    'city' : 'buea',
}

person_two = {
    'first_name' : 'john',
    'last_name' : 'doe',
    'age' : 39,
    'city' : 'chicago',
}

person_three = {
    'first_name' : 'marry',
    'last_name' : 'ann',
    'age' : 18,
    'city' : 'texas',
}

people = [person_one, person_two, person_three]


for person in people:
    print("User Info\n")
    for key, value in person.items():
        print(f'{key} : {value}\n')


print('Location for each person')

for people in people:
    print(f"{people['first_name'].title()} is {people['age']} years old and lives in {people['city'].title()}\n")
       