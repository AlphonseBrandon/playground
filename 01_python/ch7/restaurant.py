'''
Author: Alphonse Brandon
Date Created: 02-07-2023
Subject: Ch6 - Working user inputs and while loops
'''
# Restaurant seating

prompt = 'How many people are in the dinner group '
message_wait = 'You will have to wait for a table '
message_ready = 'Your table is ready '

dinner_group_input = input(prompt)

dinner_group = int(dinner_group_input)

if dinner_group > 8:
    print(message_wait)
if dinner_group <= 8:
    print(message_ready)
