# Booleans or Bool
# a variable that is either
# True or False
# - another way of thinking about this
#   - on or off
#   - 1 or 0

lightOn = False

#print(lightOn)


# conditionals
# if - elif - else
# test for a condition, if true, do code "inside" of the conditional
'''

if lightOn:
    print("Your lights are on!")
    print("this wont get executed")
    print("or this either")

print("outside of the if statement")

'''

'''
age = 999999

if age >= 18:
    print("You are old enough to drive. You are old enough to vote!")
elif age >= 16 and age < 18:
    print("You are old enough to drive, but too young to vote")
else:
    print("You are too young to drive and to vote")
'''


#list (arrays)
# every item in a list (or array) is called an 'element'
# an element's position is called its index
# ELEMENTS IN ARRAYS (LISTS) ARE ZERO INDEXED

animals = ["dogs", "cats", "monkeys", "elephants", "kangaroo"]

#print(animals)

# to get the first element, access index position 0
#print(animals[0])

# to get the second element, access indexd position 1
#print(animals[1])

# find out how many elements (items) are in your list
# len(myListName)
#print(len(animals))

#print(animals[len(animals) - 1])


# animals[5] = "lion" # this doesn't work

'''
print(animals)

animals.append("lion")

print(animals)
'''

# Strings inside lists need their own quote marks
#name = ["Adam", "Bob", "Fred"]






# loops
# while loops
# for loops
# continously running an if condtion until the condition is no longer true

age = 0
# infinite loop - USER BEWARE
'''

while age < 16:
    print("You are too young to drive")
    print("print this line too")

print("You are now old enough to drive") # this will never get exectued


    
'''
'''
while age < 16:
    print("You are too young to drive")
    age = age + 1

print("You are now 16, you can now drive")
print(age)
'''

'''
for number in range(1,17):
    print(number)
'''


animals = ["dogs", "cats", "monkeys", "elephants", "kangaroo"]

#print(animals)

for animal in animals:
    print(animal)

    













