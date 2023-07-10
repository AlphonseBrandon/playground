'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

from send_message import send_messages, sent_messages

messages = ['Hello','How are you', 'It is the month of Joy']

send_messages(messages[:])

print(f'List of draft messages:\n{messages}')
print(f'List of sent messages:\n{sent_messages}')