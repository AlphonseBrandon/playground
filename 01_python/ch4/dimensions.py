'''
Author: Alphonse Brandon
Date Created: 26-06-2023
Subject: Working with turples
'''

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# turple with one element
dimensions_one = (20,)
print(dimensions_one[0])

# looping through all values in a turple

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

print('Modified dimensions:')
dimensions = (400, 100)

for dimension in dimensions:
    print(dimension)