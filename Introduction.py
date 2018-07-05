'''
The aim of this python file is help beginners get accustomed to Python. Inspect the code and its output to better
understand data types, print statements, conditionals, and loops.
Author: Sarthak Batra


Section 1 deals with Swapping two variables
Section 2 deals with Print statements
Section 3 deals with Data types
Section 4 deals with Conditionals
Section 5 deals with Loops
'''

# Section 1: Swapping 2 variables---------------------------------------------------------------------------------------

print('Section 1: Swapping 2 variables')
print('-------------------------------\n')

v1 = "Sarthak"
v2 = "Batra"
print('Var 1 = %s\nVar 2 = %s' % (v1, v2))
print('Combined string is "%s %s"\n' % (v1, v2))

# Swap the 2 variables
temp = v1
v1 = v2
v2 = temp
print('Now we will swap the variables...\n')
print('New Var 1 = %s\nNew Var 2 = %s' % (v1, v2))
print('Combined string is "%s %s"\n' % (v1, v2))


# Section 2: Print Statements-------------------------------------------------------------------------------------------

print('Section 2: Print Statements')
print('-------------------------------\n')

# Prints Substring
print('Hello'[0:3])

# Prints items on same line
print(1, 2, 3, 'Hello')

# Prints text in different lines
print('LINE1\nLINE2\nLINE3\n')

# Escape sequences, notice how you need 3 \\\ to print 2 \\
print('C:\\\somewhere\n')

# Section 3: Data Types-------------------------------------------------------------------------------------------------

print('Section 3: Data Types')
print('-------------------------------\n')

# Data Types: String, Int, Float, List, Dict
myStr = 'Hello'
myInt = 25
myFloat = 1.3
myList = [1, 2, 3, 'Hello']
myDict = {'a': 1, 'b': 2, 'c': 3}

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myDict), myDict)

# Note the difference in the output of these two print statements
print(myStr, 'World')
greeting = myStr + ' World'
print(greeting)
print("\n")

# Section 4: Conditionals-----------------------------------------------------------------------------------------------

print('Section 4: Conditionals')
print('-------------------------------\n')

# Check if a given number is divisible by 3 or 10 or both
number = 5000
print("Let's see if the number " + str(number) + " is divisible by 3, 10, or both those numbers!")
print()

if number % 30 == 0:
    print("The number " + str(number) + " is divisible by both 3 and 10")
elif number % 3 == 0:
    print("The number " + str(number) + " is divisible by just 3")
elif number % 10 == 0:
    print("The number " + str(number) + " is divisible by just 10")
print("\n")

# Section 5: Loops------------------------------------------------------------------------------------------------------

print('Section 5: Loops')
print('-------------------------------\n')

# Check if a given number is divisible by any numbers between 1 and  10, including those two
number = 5000
print("Let's see if the number " + str(number) + " is divisible by any numbers between 1 and  10")
print()
for i in range(1, 11):
    if number % i == 0:
        print("The number " + str(number) + " is divisible by " + str(i))

print("\n")

# Check if a given number is divisible by any number between a set of two natural numbers, a and b.
number = 5000
# range(a,b) outputs numbers from a to b-1
a = 5
b = 200
print("Let's see if the number " + str(number) + " is divisible by any numbers between " + str(a) + " and " + str(b))
print()
for i in range(a, b):
    if number % i == 0:
        print("The number " + str(number) + " is divisible by " + str(i))
print('-------------------------------\n')
