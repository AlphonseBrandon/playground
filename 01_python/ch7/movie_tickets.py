'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working with while loops
'''

Between_3_and_12_fee = 10
over_12_fee = 15

prompt = 'Enter your age\n'

prompt += "Write 'end' to end the program\n\t"

active = True

while active:
    print(prompt)
    age = input()
    if age == 'end':
        break
    age = int(age)
    
    if age >= 3 and age <= 12:
        print(f'Your ticket price is ${Between_3_and_12_fee}')
    elif age > 12:
        print(f'Your ticket is ${over_12_fee}')
    else:
        print('Your ticket is free')