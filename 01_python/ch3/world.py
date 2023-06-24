'''
Author: Alphonse Brandon
Date Created: 22-06-2023
Subject: List Comprehension
'''

places = ['usa', 'canada', 'france', 'rwanda', 'south africa']

print(
    f'\nOriginal List:\n{places}'
)

alphabetical_order = sorted(places)

print(
    f'\nAlphabetical Order:\n{alphabetical_order}'
)

print(
    f'\nSee the original list has not changed:\n{places}'
)

places.reverse()

print(
    f'\nReverse Order:\n{places}'
)

places.reverse()

print(
    f'\nBack to Original Order:\n{places}'
)

places.sort()

print(
    f'\nPermanent Sort:\n{places}'
)

places.sort(reverse=True)

print(
    f'\nReversed Order Sort:\n{places}'
)

number_of_countries = len(places)

print(
    f'\nThe number of countries in the list is:\n{number_of_countries}'
)

print('\nNames of places in the list:')
for place in places:
    print(place.title())