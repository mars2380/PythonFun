# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
'''
gameControl = True
while gameControl:
    numEnter = (input("Enter a number: "))
    checkEnter = (input("Enter a number to divide by: "))
    if type(numEnter) is not int:
        gameControl = False
        print("Game Over")
    else:
        num = int(numEnter)
        check = int(checkEnter)
        if num % check == 0:
            print("{0} is Multiple of ".format(num) + str(check))
        else:
            print("{0} is Not Multiple of ".format(num) + str(check))
            if num % 2 == 0:
                print("However {0} is Even".format(num))
            else:
                print("However {0} is Odd".format(num))
'''
'''
gameControl = True
while gameControl:
    numEnter = (input("Enter a number: "))
    checkEnter = (input("Enter a number to divide by: "))
    try:
        num = str(numEnter)
        check = str(checkEnter)
        gameControl = False
        print("Game Over")
    except ValueError:
        print("again")
'''

inp = input("Please enter a score: ")
try:
    if inp.type == str:
        print("Bad score")
    elif inp == 9:
        print("A")
    elif inp == 8:
        print("B")
    elif inp == 7:
        print("C")
    elif inp == 6:
        print("D")
    elif inp == 5:
        print("F")
except:
    print("Bad scopre")
