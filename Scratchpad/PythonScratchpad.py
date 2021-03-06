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

'''
# DOWNLOADING IMAGES FROM THE INTERNET

import random
import urllib.request


def downloadWebImage(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, full_name)


downloadWebImage("https://cdn.arstechnica.net/wp-content/uploads/2017/03/GettyImages-461246108-1-800x941.jpg")
'''

'''
# READ AND WRITE FILES

fw = open('sample.txt', 'w')
# Write mode
fw.write("Some random stuff.\n")
fw.write("What are you doing here?\n")
fw.write("Third line.\n")
fw.close()

fr = open('sample.txt', 'r')
# Read mode
text = fr.read()
print(text)
fr.close()
'''

'''
# From the internet

from urllib import request

download_url = 'https://download.microsoft.com/download/4/C/8/4C830C0C-101F-4BF2-8FCB-32D9A8BA906A' \
               '/Import_User_Sample_en.csv '


def download_data(url):
    response = request.urlopen(url)
    csv = response.read().decode("utf-8-sig").encode("utf-8")
    # Remove BOM characters
    csv_str = str(csv)
    # Right now, everything is in one line
    lines = csv_str.split("\\n")
    # Split it into lines
    dest = r'data.csv'  # 'r' stands for raw string, avoids needing to escape everything
    fw2 = open(dest, 'w')
    for line in lines:
        fw2.write(line + "\n")
    fw2.close()


download_data(download_url)
'''

'''
# WEB CRAWLER (Simple)

import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = r"https://codeforces.com/contest/1360/standings/page/" + str(page)
        source_code = requests.get(url)
        # HTML format
        plain_text = source_code.text
        # Now in plaintext
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': "rated-user"}):
            href = r"https://codeforces.com" + link.get('href')
            title = link.text
            print(href)
            print(title)
        page += 1


spider(1)
'''

'''
# WEB CRAWLER (Advanced)

import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = r"https://codeforces.com/contest/1360/standings/page/" + str(page)
        source_code = requests.get(url)
        # HTML format
        plain_text = source_code.text
        # Now in plaintext
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': "rated-user"}):
            href = r"https://codeforces.com" + link.get('href')
            title = link.text
            print("\n\n"+href)
            print(title)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    # HTML format
    plain_text = source_code.text
    # Now in plaintext
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.findAll('a'):
        href = r"https://codeforces.com" + link.get('href')
        print(href)
# Can use sets to get a comprehensive and un-duplicated list of links
spider(1)
'''

'''
# EXCEPTIONS
# Not syntax errors, but errors triggered due to exceptional runtime circumstances.

while True:
    try:
        ans = int(input("What is your favourite number? "))
        print(20 / ans)
        break
    except ValueError:
        print("Enter a number!")
    except ZeroDivisionError:
        print("Zero not allowed.")
    except:
        # Not recommended
        # Catches all types of errors
        print("We don't know what went wrong")
    finally:
        # Executed no matter what
        print("End of iteration.")
'''

'''
# CLASSES AND OBJECTS
# Helps group similar variables and functions together.

class Enemy:
    life = 3

    def attack(self):
        print("\nOuch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("DEAD!")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.checkLife()
enemy1.attack()
enemy1.checkLife()
enemy1.attack()
enemy1.checkLife()
enemy2.attack()
enemy2.checkLife()
'''

'''
# INIT

class Test:

    def __init__(self):
        # Called as soon as an object of this class is declared.
        print("Hello, World!")

    def swim(self):
        print("I like to swim")


test_class1 = Test()
test_class1.swim()
test_class2 = Test()
test_class2.swim()


class Enemy:
    def __init__(self, x):
        # Used as a constructor
        self.energy = x

    def get_energy(self):
        print(self.energy)


jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
'''

'''
# CLASS VARIABLES AND INSTANCE VARIABLES

class Girl:
    # Class variable, same for all objects
    gender = 'female'

    def __init__(self, name):
        # Instance variables, defined independently for every object.
        self.name = name


g1 = Girl("Akanksha")
g2 = Girl("Manisha")
print(g1.gender)
print(g2.gender)
print(g1.name)
print(g2.name)
'''

'''
# INHERITANCE

class Parent:
    def print_last_name(self):
        print('Roberts')


class Child1(Parent):
    # All functions of Parent magically included here
    def print_first_name(self):
        print("Stella")


class Child2(Parent):
    def print_first_name(self):
        print("Stella")

    def print_last_name(self):
        # Overrides the same function from Parent
        print("Artois")


person1 = Child1()
person1.print_first_name()
person1.print_last_name()

person2 = Child2()
person2.print_first_name()
person2.print_last_name()
'''

'''
# MULTIPLE INHERITANCE

class Mario:
    def move(self):
        print("I can move")


class Mushroom:
    def eat_mushroom(self):
        print("Now I am big!")


class BigMario(Mario, Mushroom):
    # Formality to match syntax, like "Do nothing"
    pass


bm = BigMario()
bm.move()
bm.eat_mushroom()
'''

'''
# THREADING
# Use with caution and only when necessary.
# Helpful when parallelisation is possible.

import threading


class Messenger(threading.Thread):
    def run(self):
        # This function is called whenever a thread is created.
        for _ in range(100):
            # The underscore is used when we don't need a loop variable
            print(threading.current_thread().getName())


x = Messenger(name="Sender")
y = Messenger(name="Receiver")
x.start()
# Creates thread and calls the 'run' function
y.start()
'''

'''
# WORD FREQUENCY COUNTER

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for post_text in soup.findAll('div', {'class': 'topic'}):
        content = post_text.text
        words = content.lower().split()
        print(words)
        for word in words:
            word_list.append(word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    symbols = "`1234567890-=~!@#$%^&*()_+,./;'[]\\<>?:\"“{}|»–—"
    for word in word_list:
        # Removal of nonsensical symbols
        for i in range(len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, ":", value)


start('https://codeforces.com/')
'''

'''
# LAMBDA
# Small function that has no name. For one-time use, unlike a function.


answer = lambda x: x * 7
print(answer(5))
'''

'''
# ARGS and KWARGS
# * args and **kwargs

def foo1(required, *args, **kwargs):
    # Here, one argument is necessary.
    # *args collects all the extra positional arguments.
    # **kwargs collects all the extra keyword arguments.
    print("\n", required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# foo1() -> Gives error
foo1("Hello")
foo1("Hello", 1, 2, 3)
foo1("Hello", 1, 2, 3, x=10, y=20)


# Helps us write wrapper functions
def foo2(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *args, **kwargs)


def bar(required, *args, **kwargs):
    print("\n", required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo2("Hello")
foo2("Hello", 1, 2, 3)
foo2("Hello", 1, 2, 3, a=10, b=20)
'''

'''
# MERGING LISTS AND DICTIONARIES

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "B": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
'''

'''
# CALLABLE OBJECTS

class Adder:
    def __init__(self, n):
        print("HI")

    def __call__(self, x):
        print("HELLO")


plus_3 = Adder(3)
plus_3(4)
print(callable(plus_3))
z = 2
print(callable(z))
'''

'''
# DECORATORS
# Temporary change/extension to a function

def null_decorator(func):
    return func


def greet1():
    return 'Hello!'


@null_decorator
def greet2():
    return 'Hello!'


def uppercase(func):
    def to_upper():
        return func().upper()

    return to_upper


@uppercase
def greet3():
    return 'Hello!'


greet1 = null_decorator(greet1)
print(greet1())
print(greet2())
print(greet3())


# Nested Decorators
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'


print(greet())
'''

'''
# SCOPE OF VARIABLES

x = 1  # x is a global variable
y = 5  # y is a global variable


def f():
    global y
    x = 2  # x is a local variable
    y += 1  # Reassigning the global variable y
    z = 10  # z is a local variable
    print("Local variable x =", x)
    print("Global variable y =", y)
    print("Local variable z =", z)


f()
print("Global variable  x =", x)
print("Global variable y =", y)
'''

'''
# RANGE VS ENUMERATE

x = [1, 5, 32, 45, 2, 112, 32]
for i in range(len(x)):
    print(i)
for i, num in enumerate(x):
    print(i)
print(list(range(len(x))))
print(list(enumerate(x)))
'''

'''
# CLASS METHODS, STATIC METHODS and INSTANCE METHODS

class MyClass:

    def method(self):
        # Also known as plain methods.
        # Can modify object instance state as well as class state.
        print("Instance method", self)

    @classmethod
    def classmethod(cls):
        # Can only modify class state.
        print("Class method", cls)

    @staticmethod
    def staticmethod():
        # No modification possible
        print("Static method")


obj = MyClass()
obj.method()
obj.classmethod()
obj.staticmethod()

MyClass.classmethod()
MyClass.staticmethod()

# MyClass.method() -> Generates error.

import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


pizza1 = Pizza(4.5, ['cheese'])
print(pizza1)
print(pizza1.area())
'''

'''
# ITERATOR

my_list = [23, 21, 3, 2, 340]
for i in my_list:
    print(i)

# This can also be accomplished using the following:
my_iterator = iter(my_list)
print(type(my_iterator))
while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break
'''

'''
# FILTER
# Applies a function to each item in the iterable and checks with criteria.

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
'''

'''
# MAP
# Takes a function and applies it to every item of an iterable.

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

# Now, let's look at a better way.

mapped_prices = []
x = map(lambda item: item[1], items)
for item in x:
    mapped_prices.append(item)
print(mapped_prices)

# Now, let us look at the best way.

mapped_prices2 = list(map(lambda item: item[1], items))
print(mapped_prices2)
'''

'''
# GENERATORS

def square_nums(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_list = square_nums([1, 2, 3, 4, 5])
print(my_list)


# Conversion to generator

def square_nums(nums):
    for i in nums:
        yield i * i


my_gen = square_nums([1, 2, 3, 4, 5])
for num in my_gen:
    print(num)

# list can also be created using list comprehensions
my_list = [x * x for x in [1, 2, 3, 4, 5]]

# Generators are similar to this
my_gen = (x * x for x in [1, 2, 3, 4, 5])
'''

'''
# POLYMORPHISM
# Same method name with different parameter lists.

print(6 * 5)
print("Repeat" * 4)
'''

'''
# ABSTRACT CLASSES

class Computer1:
    def process(self):
        # This is an abstract method, and hence this class becomes abstract.
        pass


# Python, by default, does not support abstract classes
# So, we need a workaround

from abc import ABC, abstractmethod


class Computer2(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop1(Computer2):
    pass


class Laptop2(Computer2):
    def process(self):
        print("OH YEAH!")


com1 = Computer1()
# com2 = Computer2() -> Gives error, can't instantiate abstract classes.
# com3 = Laptop1() -> Gives error, abstract methods not implemented
com4 = Laptop2()
com4.process()
'''

'''
# DATETIME

import datetime

x = datetime.datetime.now()
print(x)
print("The year is {}".format(x.year))
print("The month is {}".format(x.month))

# Create a date manually
new_date = datetime.datetime(1998, 11, 4)
print(new_date)
new_keyword_date = datetime.datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
print(new_keyword_date)
# Month full name
print(new_date.strftime("%B"))
# Month short name
print(new_date.strftime("%b"))
# Weekday full name
print(new_date.strftime("%A"))
# Weekday short name
print(new_date.strftime("%a"))
# Day of the month
print(new_date.strftime("%d"))

import time

x = time.time()
print(x)

# Combine date and time
today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)
curr_time = datetime.time(now.hour, now.minute, now.second)
print(curr_time)
combined = datetime.datetime.combine(today, curr_time)
print(combined)
'''

'''
# JSON

import json

# JSON to Python dict
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# Stored as a dictionary
print(y)
print(y["age"])

# Python dict to JSON
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)

# Other data types
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Print formatted JSON
print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))
'''

'''
# 12 DIGIT ALPHANUMERIC UID GENERATOR

import random
import string
import os

# Check if file already exists
if not os.path.exists('id.txt'):
    # Create if it doesn't
    open('id.txt', 'w').close()

# Get contents of file
fr = open('id.txt', 'r')
curr_set = fr.read().split()

# Create list with already existing IDs
already_allocated = []
for i in curr_set:
    already_allocated.append(str(i))

# Allocate a new ID
while True:
    x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    if x not in already_allocated:
        # Append to the file
        open("id.txt", 'a').write(x + " ")
        break
'''

'''
# CHECK IF A DICTIONARY IS CONTAINED IN ANOTHER

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.items() <= dict2.items())
'''

'''
# SORT A DICTIONARY ON THE VALUES

unsorted_dict1 = {'Kabir': 'Boy', 'Leader': 'Archit', 5: 'Five', 'Company': 'Innovaccer'}
unsorted_dict2 = {1: 2000, 4: 3, 2: -3, 'Zero': 0}
while True:
    try:
        sorted_dict = {k: v for k, v in sorted(unsorted_dict1.items(), key=lambda item: item[1])}
        break
    except TypeError:
        print("Dictionary values should only contain string or int. Stick to one type")
print(sorted_dict)
'''

'''
# SORT A LIST OF DICTIONARIES, ON TWO FIELDS

input_dict_list = [{'name': 'Francis', 'age': 65}, {'name': 'Aron', 'age': 40}, {'name': 'Mike', 'age': 45}, {'name': 'Bran', 'age': 31}, {'name': 'James', 'age': 35}, {'name': 'Rick', 'age': 36}, {'name': 'Mike', 'age': 35}, {'name': 'James', 'age': 43}]
final_dict_list = sorted(sorted(input_dict_list, key=lambda k: k['name']), key=lambda k: k['age'])
print(final_dict_list)
'''

'''
# CACHE FUNCTION OUTPUT USING A DECORATOR
# Similar to DP

import functools


@functools.lru_cache(maxsize=1024)
def fibonacci(n):
    # Expensive function - (2^n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))
print(fibonacci(100))
print(fibonacci(300))
'''

'''
# UNPACK LISTS/TUPLES

month, item, price = ['December', 'Cue Stick', 1500]
# Ensure the number of variables and items are the same
print(item)


# What to do with different sizes?
def drop_first_last(grades):
    first, *mid, last = grades
    print(sum(mid) / len(mid))


my_list_grades = [12, 2, 3, 4, 5, 6, 7, 81]
drop_first_last(my_list_grades)
'''

'''
# ZIP

first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)
for a, b in names:
    print(a, b)
'''

'''
# MIN, MAX AND SORTING DICTIONARIES

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZA': 306.21,
    'AAPL': 99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

# Multiple key sort

from operator import itemgetter

users = [
    {'name': 'Francis', 'age': 65},
    {'name': 'Aron', 'age': 40},
    {'name': 'Mike', 'age': 45},
    {'name': 'Bran', 'age': 31},
    {'name': 'James', 'age': 35},
    {'name': 'Rick', 'age': 36},
    {'name': 'Mike', 'age': 35},
    {'name': 'James', 'age': 43}
]

users = sorted(users, key=itemgetter('age'), reverse=True)
users = sorted(users, key=itemgetter('name'))
# Sorting is stable
print(users)
'''

'''
# SORTING CUSTOM OBJECTS

from operator import attrgetter


class User:
    def __init__(self, name, uid):
        self.name = name
        self.user_id = uid

    # String representation of class
    def __repr__(self):
        return self.name + "\t:\t" + str(self.user_id)


users = [
    User('Kabir', 411),
    User('Kanha', 98),
    User('Arora', 69),
    User('Shiv', 1000),
    User('Nadar', 54)
]

for user in users:
    print(user)

print('-----------')

for user in sorted(users, key=attrgetter('name')):
    print(user)
'''

'''
# HTML TO PDF CONVERTER
# Apart from installing pdfkit, also need to download wkhtmltopdf and add to PATH.

import pdfkit

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_url('https://www.codeforces.com/', 'out.pdf', configuration=config)
pdfkit.from_file('test.html', 'test.pdf', configuration=config)
'''

'''
# ASYNCIO

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
'''
