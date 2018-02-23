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

