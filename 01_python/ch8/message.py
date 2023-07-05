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

def make_album(name='Loveworld Singers', title='Praise Night 14', songs=None):
    album = {}
    if songs:
        album['name'] = name
        album['title'] = title
        album['songs'] = songs
    else:
        album['name'] = name
        album['title'] = title
    return album

album = make_album()
print(album)
album = make_album('Choir', 'Praise Service', 13)
print(album)
print(f'The data structure is of type: {type(album)}')



def orders():
    while True:
        orders = {}
        print('To quit the program, enter "q"')
        name = input('Enter your name: ')
        if name == 'q':
            break
        food = input("what's your favourite food?")
        if food == 'q':
            break
        orders['name'] = name
        orders['food'] = food
        return orders
        
orders = orders()
print(orders)
print('Food ordered')
for name, food in orders.items():
    print(f'{orders[name]} your order has been confirmed')

message_list = ['Hello', 'how', 'are you', 'home']

def show_messages(messages: list) -> None:
    for message in messages:
        print(message)
show_messages(message_list)

sent_messages = []
def send_messages(messages: list, sent_messages: list) -> None:
    for message in messages:
        print(f'Sending: {message}')
        sent_messages.append(message)
    for sent_message in sent_messages:
        print(f'Sent: {sent_message}')
send_messages(message_list, sent_messages)

print('List of messages:\n\t')
print(message_list)

print('List of sent messages')
print(sent_messages)



