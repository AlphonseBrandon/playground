'''
Brandon
Date Created: 10-07-2023
Subject: Ch10 - Files and exceptions
'''

print('Enter two intergers')
num1 = input('Enter first number: ')
num2 = input('Enter second Number ')

try:
    addition = int(num1) + int(num2)
except ValueError:
    print('Please enter a valid integer')
else:
    print(f'The sum of the two numbers is {addition}')
