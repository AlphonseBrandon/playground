'''
Author: Alphonse Brandon
Date Created: 30-06-2023
Subject: Working with dictionaries
'''

rivers = {
    'egypt' : 'Nile',
    'cameroon' : 'sanaga',
    'cameroon' : 'wouri',
}

for country, river in rivers.items():
    print(f'{river.title()} runs through {country.title()}')

print('Name of each river in the dictionary:')

for river in rivers.values():
    print(river)