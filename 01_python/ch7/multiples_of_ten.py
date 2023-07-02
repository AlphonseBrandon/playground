'''
Author: Alphonse Brandon
Date Created: 02-07-2023
Subject: Ch6 - Working user inputs
'''

prompt = 'Input a number'
prompt += '\nI will tell you if the number is a multiple of 10 '


number_inputed = input(prompt)
number = int(number_inputed)

message_yes = f'{number} is a multiple of 10'
message_no = f'{number} is not a multple of 10'

if (number % 10 == 0):
    print(message_yes)
if (number % 10 != 0):
    print(message_no)