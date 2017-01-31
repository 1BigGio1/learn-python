#Learn Python
####Notes from the January 2017 Coding-For-Teens program

This repository contains the source code from the Coding for Teens program at the Oak Harbor Library done in January 2017. This page serves as a review of the material covered during the 4 sessions. View a file to see more in depth information.

###Comments
a programmer-readable explanation in the source code of a computer program. The computer ignores comments. Can be single line comments or multi-line comments
```python
# single line comments
'''
multi
line
comments
'''
```

###Strings
words and text. May be enclosed in double quotes or single quotes
```python
print("Hello, World!")
print('Hello, World!')

firstName = "Adam"
print(myName)
# Adam

lastName = 'Allard'
print(firstName, lastName)
# Adam Allard

fullName = firstName + ' ' + lastName
print(fullName)
# Adam Allard
```

### Integers and Floats
```python
# Integers are whole numbers
# 1, 2, 3, 0, -968, 9485
myAge = 25

# Floats are decimal numbers
# 1.0, 3.14, 1.99, -0.563, 999.99
avocado = 6.02
```


### Math
```python
# addition
print("5 + 2 =", 5 + 2)
# 7
# notice that "5 + 2 =" is a string
# notice that 5 + 2 is a computation

# subtraction
print("5 - 2 =", 5 - 2)
# 3

# multiplication
print("5 * 2 =", 5 * 2)
# 10

# division
print("5 / 2 =", 5 / 2)
# 2.5

# modulus - gives the remainder after division
print("5 % 2 =", 5 % 2)
# 1

# exponents - 5 raised to the 2nd power
print("5 ** 2 =", 5 ** 2)
# 25

# floor division - how many times will 2 evenly go into 5?
print("5 // 2 =", 5 // 2)
# 2
```



### Booleans
A variable that's either True or False
```python
# Boolean
# True or False
# on or off
# 1 or 0

# if I turn my light switch off
lightSwitch = False

# when I flip the switch on
lightSwitch = True
```



### if, elif, else
Test for a condition, if it's True, execute the if statement
```python
lightSwitch = False

if lightSwitch:
    print("Your lights are on!")
else:
    print("Your lights are off!")
    
age = 25

if age >= 18:
    print("You are old enough to drive. You are old enough to vote.")
elif age >= 16 and age < 18:
    print("You are old enough to drive.")
elif age < 16 and age >= 0:
    print("You are too young to drive, too young to vote.")
else:
    print("Your age is incorrect.")
```


### While Loop
Execute certain lines of code an unknown number of times
```python
age = 13

while age < 16:
    print("You are", age, "years old. You are too young to drive.")
    
    # A year passes by
    print("Happy Birthday!")
    age = age + 1
    
print("You are now", age, "years old!. You are now old enough to drive!")

# You are 13 years old. You are too young to drive.
# Happy Birthday!
# You are 14 years old. You are too young to drive.
# Happy Birthday!
# You are 15 years old. You are too young to drive.
# Happy Birthday!
# You are now 16 years old!. You are now old enough to drive!
```

###Lists
```python
groceryList = ['apples', 'bananas', 'eggs', 'milk', 'cheese']
# Each item in a list is called an element
# Each element in a list has a position
# A position in a list is called an index
# The first element in a list is at index 0
# The second element in a list is at index 1

print(groceryList[0])
# apples
print(groceryList[1])
# bananas
print(groceryList[4])
# cheese
```


###For Loops
Execute certain lines of code a known number of times
```python
groceryList = ['apples', 'bananas', 'eggs', 'milk', 'cheese']

for groceryItem in groceryList:
    print(groceryItem)
# apples
# bananas
# eggs
# milk
# cheese

# print the numbers 1 - 100
for number in range(1, 101):
    print(number)
# 1
# 2
# ...
# 100
```


###Functions
pieces of code that can be called later
```python
# can be a stand alone function. no arguements, no return value
def helloWorld():
    print("Hello, World!")
    
helloWorld()
# Hello, World!

# -----------------------------

# can accept arguements
def add(num1, num2):
    print(num1, '+', num2, '=', num1 + num2)
    
add(3, 7)
# 3 + 7 = 10

# -----------------------------

# can return a value
def add(num1, num2):
    return num1 + num2
    
sum = add(5, 5)
print(sum)
# 10

# -----------------------------

# can call another function

def secondFunction():
    print("I'm in the second function now!")

def firstFunction():
    print("This is the first function.")
    print("I will now call the second function.")
    secondFunction()
    print("I'm back in the first function")
    
print("This line will print first.")
firstFunction()
print("Ok, I'm done calling functions now.")
# This line will print first.
# This is the first function.
# I will now call the second function.
# I'm in the second function now!
# I'm back in the first function
# Ok, I'm done calling functions now. 
```





