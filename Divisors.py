'''
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''
num = int(input("Enter a number to divide by: "))
var1, var2 = [int(x) for x in input("Enter two numbers to make a list here: ").split()]
var2 = var2 + 1
x = range ( var1, var2 )
for elem in x:
    if elem % num == 0:
        print(elem)
