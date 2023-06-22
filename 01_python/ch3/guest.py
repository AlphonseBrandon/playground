'''
Author: Alphonse Brandon
Date Created: 22-06-2023
Subject: List Comprehension
'''

guests = ['alphonse', 'brandon', 'john', 'doe']

message1 = f'Hello {guests[0].title()} you are invited'

print(message1)

absent = guests[1]

message2 = f"So sorry {absent.title()} can't make it"

print(message2)

guests[1] = 'trump'

message3 = f'Welcome {guests[1].title()} you are invited'

print(message3)

guests.insert(0, 'mary')

guests.insert(2, 'glory')

guests.append('wick')

message4 = f'Hi {guests[-1].title()} you are invited'

print(message4)

message5 = "Oh, sorry, I can invite only two guest"

print(message5)

guests.pop()
guests.pop()
guests.pop()
guests.pop()

message6 = f'Congratulations {guests[0].title()} and {guests[1].title()} you have been invited'

print(message6)

del guests[0]
del guests[1]
guests.remove('alphonse')

message7 = f'The party is over {guests}'

print(message7)
