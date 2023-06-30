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

print('Rivers and countries dictionary\n')
for country, river in rivers.items():
    print(f'{river.title()} runs through {country.title()}')

print('\nName of each river in the dictionary:\n')

for river in rivers.values():
    print(river)

print('\nName of each country in the dictionary:\n')

for country in rivers.keys():
    print(country.title())