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
