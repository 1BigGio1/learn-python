'''
Converter program

Convert between different units of measurement
'''

playAgain = True
while playAgain:

    print("=========================================")
    print("Welcome to Measurements Converter Program")
    print("=========================================")

    print("What metric are you trying to convert?")
    print(" 1. Length")
    print(" 2. Weight")
    print(" 3. Temperature")
    metric = input(": ")
    metric = metric.upper()

    if metric == "1" or metric == "LENGTH":
        print("do length conversion here")
        # this is part of your assignment
    elif metric == "2" or metric == "WEIGHT":
        print("do weight convers")
    elif metric == "3" or metric == "TEMPERATURE":
            
        # F -> C = 5/9 * (F - 32)
        # C -> F = 9/5 * C + 32

        print("What unit are you starting out with?")
        unit = input("F/C: ")

        print("How many degrees", unit, "do you have?")
        degrees = float(input(": "))

        # fix user input
        unit = unit.upper()

        # create new vars to convert to
        newUnit = "F" # might not stay F
        newDegrees = -999.0 # might not stay -999.0

        # = does not equal ==
        # = is for assignments
        # == is for testing conditions (is equal to?)
        if unit == "F":
            newUnit = "C"
            newDegrees = 5/9 * (degrees - 32)
        elif unit == "C":
            newUnit = "F"
            newDegrees = 9/5 * degrees + 32
        else:
            print("error - you entered wrong data")

        print(degrees, unit, "is equal to", newDegrees, newUnit);


    print("Do you want to make another conversion?")
    answer = input("(Y/N): ")

    if answer.upper() == "N":
        playAgain = False

print("Thank you for using my program. Good bye!")




    
    



