'''
Author: Alphonse Brandon
Date Created: 22-06-2023
Subject: List Comprehension
'''

numbers = [number for number in range(1, 21,2)]

print(f'Odd numbers from 1 to 20:\n{numbers}')

threes = []
for three in list(range(3,31)):
    threes.append(three*3)
print(f'Multiples of three from 1 to 31 range:\n{threes}')


digits = [digit for digit in range(1, 1000001)]

minimum = min(digits)
maximum = max(digits)
summation = sum(digits)

print(
    f'''Within the range of one to one million\n
    \tMinimum number: {minimum}\n
    \tMaximum number: {maximum}\n
    '''
)