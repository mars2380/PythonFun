import datetime
now = datetime.datetime.now()
year = now.year

name = input("Give me your name: ")
print("Your name is " + name)

age = int(input("Enter your age: "))
#if age.is_integer():
#    print(fff)

print("Your age is " + str(age))

oldyear = str((year - age)+100)
print(name + " will be 100 years old in the year " + oldyear)

# Some shit test
def shit ():
    print("Were " + "wolf")
    print("Door " + "man")
    print("4 " + "chan")
    print(str(4) + " chan")
    print(4 * "test ")


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
