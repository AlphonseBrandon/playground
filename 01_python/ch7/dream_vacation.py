'''
Author: Alphonse Brandon
Date Created: 03-07-2023
Subject: Ch6 - Working with while loops
'''




print('If you could visit one place in the world, where will it be')

vacations = {}

while True:
    print('Enter your name please \n')
    name = input()
    print('Enter the place you wish to visit\n')
    vacation = input()
    vacations[name] = vacation
    print('Do you want to enter more places? reply "yes/no"')
    state = input()
    if state == 'no':
        break

for name, vacation in vacations.items():
    print(f'{name.title()} wishes to go on vacation to {vacation.title()}')
