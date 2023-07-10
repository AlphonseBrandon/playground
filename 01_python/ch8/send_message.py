'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

drafts = ['Hello', 'Good Morning', 'How are you?']

def show_messages(drafts: list) -> None:
    """Print each text message stored in drafts"""
    for draft in drafts:
        print(draft)

sent_messages = []

def send_messages(drafts: list) -> None:
    "Move the messages from draft to send_messages list"
    while drafts:
        message = drafts.pop()
        print(f'Sending {message}')
        sent_messages.append(message)

send_messages(drafts=drafts)

print(f'List of draft messages:\n{drafts}')
print(f'List of sent messages:\n{sent_messages}')

