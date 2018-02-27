'''
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
gameControl = True
while gameControl:
    try:
        num = int(input("Enter a number: "))
        check = int(input("Enter a number to divide by: "))
        gameControl = False
        if num % check == 0:
            print ( "{0} is Multiple of ".format ( num ) + str ( check ) )
        else:
            print ( "{0} is Not Multiple of ".format ( num ) + str ( check ) )
            if num % 2 == 0:
                print ( "However {0} is Even".format ( num ) )
            else:
                print ( "However {0} is Odd".format ( num ) )
    except:
        print ("This is not a number! Do not to be stupid!!!!!")
