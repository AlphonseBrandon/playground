'''
Author: Alphonse Brandon
Date Created: 21-06-2023
Subject: Understand how strings work in python - exercises
'''

'''
1. Personal Message: Use a variable to represent a person’s name, and
print

'''
print("\nTask 1:\n\t")

name = "alphonse"
message = f"Hello {name.title()} would you like to learn some Python today?"
print(message)

'''
2. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.

'''

print("\nTask 2:\n\t")

full_name = "alphonse brandon"
small_letters = full_name.lower()
big_letters = full_name.upper()
camelcase = full_name.title()

message = f"UpperCase: \n\t{big_letters} \nLowerCase: \n\t{small_letters} \nTitleCase \n\t{camelcase}"

print(message)

'''
3.  Famous Quote: Find a quote from a famous person you admire. Print
the

'''

print("\nTask 3:\n\t")

famous_person = "Albert Einstein"

message = f'{famous_person} once said "A person who never made a mistake never tried anything"'

print(message)

'''
4. Stripping Names: Use a variable to represent a person’s name, and
include a white space at the biggining and end of the name

'''

print("\nTask 3:\n\t")

whitespace_name = "\t Alphonse Brandon\t"

no_right_whitespace = whitespace_name.rstrip()

no_left_whitespace = whitespace_name.lstrip()

no_space_between = whitespace_name.strip()

print(
    f'''
    Whitespace name: {whitespace_name}\n
    Right whitespace removed: {no_right_whitespace}\n
    Left whitespace removed: {no_left_whitespace}\n
    Left and right whitespace removed: {no_space_between}
    '''
)