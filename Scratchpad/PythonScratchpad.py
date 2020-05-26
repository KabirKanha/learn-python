"""
# IF-ELIF-ELSE
age = 13
if age < 21:
    print("Too bad")
else:
    print("Have a beer")
name = "Kabir"
if name is "Bucky":
    print("NO")
elif name is "Kabir":
    print("OH YES")
else:
    print("WHO DIS")
"""

'''
# FOR LOOP
foods = ['bacon', 'tuna', 'sausages', 'beef']
for item in foods[:2]:
    print(item)
    print(len(item))
'''

'''
# RANGE
for x in range(5, 12, 2):
    print(x)
    # print("Haha")
'''

'''
# WHILE
x = 5
while x < 20:
    print(x)
    x += 1
'''

''' 
# BREAK
someNumber = 26
for n in range(101):
    if n is someNumber:
        print("Hurray, found", someNumber)
        break
    else:
        print(n)
'''

'''
# CONTINUE
numbers = [2, 5, 12, 33, 17]
print("Available numbers:")
for n in range(20):
    if n in numbers:
        print(n)
        continue
'''

'''
# FUNCTIONS


def foo():
    print("Good job, son")


def miles_to_km(miles):
    print(miles * 1.6)


def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age


def get_gender(sex='Unknown'):
    if sex == 'm':
        sex = 'Male'
    elif sex == 'f':
        sex = 'Female'
    print(sex)


foo()
miles_to_km(300)
miles_to_km(31)
print(allowed_dating_age(21))
get_gender('m')
get_gender('f')
get_gender()
'''

'''
# SCOPE

s = 7823


# If variable outside function and above it, function can use it.
def corn():
    x = 5
    print(x)
    print(s)


def fudge():
    print(s)
#     print(x)
#     Variables defined in another function are not available.
'''

'''
# KEYWORD ARGUMENTS


def dumb_sentence(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)


dumb_sentence()
dumb_sentence('Kabir', 'went', 'gymming')
dumb_sentence(name='Archit')
dumb_sentence('chicken')
dumb_sentence(item='chicken')
'''

'''
# FLEXIBLE NUMBER OF ARGUMENTS


def add_numbers(*args):
    # Can be named anything, not necessarily args.
    total = 0
    for i in args:
        total += i
    print(total)


add_numbers(3)
add_numbers(5, 3, 12, 45, 32)
'''

'''
# UNPACKING ARGUMENTS


def health_calculator(age, apples, cigs):
    healthRating = (100 - age) + (apples * 3.5) - (cigs * 2)
    print(healthRating)


kabir_health_data = [21, 20, 0]
health_calculator(kabir_health_data[0], kabir_health_data[1], kabir_health_data[2]
# Is there a faster way?
health_calculator(*kabir_health_data)
# The * does the same thing internally. Saves us the effort.
'''

'''
# SETS
# A collection of items without duplicates.

groceries = {'cereal', 'milk', 'beer', 'tape', 'lotion', 'milk'}
# Milk printed just once.
print(groceries)
# Order not preserved
'''

'''
# DICTIONARY
# Similar to a map (has key-value pairs)

classmates = {'Tony': 'cool but quiet', 'Emma': 'sits behind me', 'Lucy': 'asks too many questions'}
print(classmates)
print(classmates['Emma'])
# Quick way to loop through:
for k, v in classmates.items():
    print(k + " - " + v)
'''

'''
# MODULES
# Write functions to be used in another file and just include that file.

import HelperFunctions
import random

# fish() will not work
HelperFunctions.fish()
# Modules help us use pre-existing functions and those created by other people.
x = random.randrange(1, 1000)
print(x)
'''