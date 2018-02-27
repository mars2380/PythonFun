'''
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime

now = datetime.datetime.now()
year = now.year

name = input("Give me your name: ")
print("Your name is " + name)

valid_input = False
while not valid_input:
    age = (input("Enter your age: "))
    try:
        val = int(age)
        valid_input = True
    except ValueError:
        print("That's not a correct age!")

print("Your age is " + str(val))

oldyear = str((year - val)+100)
print(name + " will be 100 years old in the year " + oldyear)

# Some shit test
def shit ():
    print("Were " + "wolf")
    print("Door " + "man")
    print("4 " + "chan")
    print(str(4) + " chan")
    print(4 * "test ")

