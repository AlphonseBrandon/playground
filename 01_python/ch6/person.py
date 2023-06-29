'''
Author: Alphonse Brandon
Date Created: 28-06-2023
Subject: Working with dictionaries
'''
# Bio info
person = {
    'first_name' : 'alphonse',
    'last_name' : 'brandon',
    'age' : 30,
    'city' : 'buea',
}

print(f'First Name : {person["first_name"].title()}')

# Favourite Number

favourite_number = {
    'alphonse':7,
    'brandon':8,
    'njei':10,
    'tom': 5,
}

print('Names and favourite numbers')
for key, value in favourite_number.items():
    print(f'{key.title()} : {value}\n')

# print(f'Alphonse favourite number is {favourite_number["alphonse"]}')

message = 'Name of everyone with favorite number'

print(message)

friends = ['alphonse', 'brandon']
for name in favourite_number.keys():
    if name in friends:
        print(f'Hey {name.title()} I see your favourite number is {favourite_number[name]}')
    else:
        print(name.title())

   
