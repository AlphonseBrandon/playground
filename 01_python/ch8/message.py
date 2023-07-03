'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working functions
'''

def display_message():
    print('Hi, I am currently learning Python!')

display_message()

def favourite_book(book):
    print(f'One of my favourite books is {book}')
favourite_book('The Power of your Mind')

def make_shirt(text='I love Python',size='large'):
    print(f'The size of the shirt is {size} and you want the following message printed on it: \n"{text}"')


message = 'Education is a powerful weapon'

make_shirt()

print('\n Country city format')
def city_country(city='Buea', country='Cameroon'):
    return f"{city.title()}, {country.title()}"

country_city = city_country()

print(country_city)


print('\nAlbum dictionary')

def make_album(name='Loveworld Singers', title='Praise Night 14'):
    album = {name:title}
    return album

album = make_album()
print(album)
print(f'The data structure is of type: {type(album)}')