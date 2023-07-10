'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

import send_message as sm

# messages = ['Hello','How are you', 'It is the month of Joy']

sm.send_messages(drafts=sm.drafts[:])

print(f'List of draft messages:\n{sm.drafts}')
print(f'List of sent messages:\n{sm.sent_messages}')