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
show_messages(drafts=drafts)
