#print("Jamie Wai")
#print('o----')
#print('||||')
#print('*' * 10)

#price = 10
#rating = 4.9
#name = "Jamie"
#is_published = False
#print (price)

#full_name = "John Smith"
#age = 39
#gender = "Male"
#is_new = True

#name = input('What is your name?')
#print('Hi' + name)

#name = input('What is your name?')Jamie
#colour = input('What is your favourite colour?')
#print(name + ' likes ' + colour)

#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2021 - int(birth_year)
#print(type(age))
#print(age)

#weight_pounds = input('What is your weight in pounds?')
#weight_kg = 0.45 * int(weight_pounds)
#print(weight_kg)

#weight_lbs = input('Weight (lbs): ')
#weight_kg = 0.45 * int(weight_lbs)
#print(weight_kg)

#course = "Python's Course for Beginners"
#print(course)

#greeting = '''
#Hi John,

#Here is our first email to you.

#Thank you,
#Jamie
#'''
#print(greeting)

#course = 'Python for Beginners'
#print(course[-3])
#print(course[0:5])
#print(course[2:])
#print(course[:10])

#name = 'Jennifer'
#print(name[1:-1])

#first = 'John'
#last = 'Wick'
#message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)

#name = 'Jamie Lau Tsun Wai'
#print(len(name))
#print(name.upper())
#print(name.lower())
#print(name.find('s'))
#print(len(name))
#print(name.replace('Wai', 'Wei'))
#print('lau' in name)


# CACULATION - ARITHMETIC OPERATORS, OPERATOR PRECEDENCE, MATH FUNCTION

## Two kind of division
### 01- a foward slash - will fet a floating point number
#print(10/3)
### 02 - two forward slashes - getting an integer
#print(10//3)

## Modulus
#print(10%3)

## Exponent which is the power
#print(10**3) #it is indicated with 2 asterisks 

## augmented assignment operator
#x = 10
#x = x + 3
#x -= 3 #the augmented operator 
#print(x)

## OPERATOR PRECEDENCE
#x = 10 + 3*2**2
#print(x)
#x = (10 + 3) * 2 ** 2
#print(x)
### Order of operations
### expomemtiation 2**3 --> multiplication or division -->addition or subtraction
### parenthesis always takes priority

## Math function
#x = 2.9
#print(round(x))
#x = -5.6
#print(abs(x))
### Math module
#import math
#print(math.ceil(5.6)) # ceil method
#print(math.floor(5.6)) # floor method


# IF STATEMENT
##is_cool = False
##is_hot = False

##if is_cool:
    #print("It's a cool day")
    #print('Have an icecream')
##elif is_hot:
    #print("It's a hot day")
    #print('Wear shorts')
##else:
    #print("It's a beautiful day") 
##print('Make each day count')
#PRACTISE:
##price = 1000000
##has_good_credit = True

##if has_good_credit:
    ##down_payment = 0.1 * price
##else:
    ##down_payment = 0.2 * price

##print(f"Down payment: ${down_payment}")


# LOGICAL OPERATORS

##having_high_income = True
##having_good_credit = True

##if having_high_income and having_good_credit:  # AND: both
    ##print("Eligible for loans")

##having_high_income = False
##having_good_credit = True

##if having_high_income or having_good_credit:     # OR: at least one
    ##print("Eligible for loans")

##having_criminal_records = False
##having_good_credit = True

##if having_good_credit and not having_criminal_records:     # and not: both
    ##print("Eligible for loans")


# COMPARISON OPERATORS

