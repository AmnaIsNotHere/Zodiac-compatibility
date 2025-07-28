'''
zodiac compatibility test
author: <Amna Ali>
course: ICS3UC
date: <21/11/2024>
'''

# make subprogram for getting someones bithday

def birthday():

    valid = True
    year = 0

    while valid:
        year = int(input("Enter the year you were born in 4 integer format: "))

        if (year <= 2025):
            valid = False

        else:
            print("enter a number below 2026")


    valid2 = True

    while valid2:
        month = input("Enter the month you were born: ")

        if month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
            valid2 = False

        else:
            print("enter month name in 3 letter, and first has to be upper case")


    valid3 = True
    day = 0

    while valid3:

        day = int(input("Enter the day you were born: "))

        if (day <= 31):
            valid3 = False

        else:
            print("enter a date below 32")

    return year, month, day

# make subprogram one for determining zodiac

def zodiac(year, month, day):
    zodiac = "zodiac"

    if (year - 1900) % 12 == 0:
        if month == "jan":
            zodiac = "pig"
        else:
            zodiac = "rat"

    elif (year - 1901) % 12 == 0:
        if month == "jan":
            zodiac = "rat"
        else:
            zodiac = "ox"

    elif (year - 1902) % 12 == 0:
        if month == "jan":
            zodiac = "ox"
        else:
            zodiac = "tiger"

    elif (year - 1903) % 12 == 0:
        if month == "jan":
            zodiac = "tiger"
        else:
            zodiac = "rabbit"

    elif (year - 1904) % 12 == 0:
        if month == "jan":
            zodiac = "rabbit"
        else:
            zodiac = "dragon"

    elif (year - 1905) % 12 == 0:
        if month == "jan":
            zodiac = "dragon"
        else:
            zodiac = "snake"

    elif (year - 1906) % 12 == 0:
        if month == "jan":
            zodiac = "snake"
        else:
            zodiac = "horse"

    elif (year - 1907) % 12 == 0:
        if month == "jan":
            zodiac = "horse"
        else:
            zodiac = "goat"

    elif (year - 1908) % 12 == 0:
        if month == "jan":
            zodiac = "goat"
        else:
            zodiac = "monkey"

    elif (year - 1909) % 12 == 0:
        if month == "jan":
            zodiac = "monkey"
        else:
            zodiac = "rooster"

    elif (year - 1910) % 12 == 0:
        if month == "jan":
            zodiac = "rooster"
        else:
            zodiac = "dog"

    elif (year - 1911) % 12 == 0:
        if month == "jan":
            zodiac = "dog"
        else:
            zodiac = "pig"

    return zodiac


# make subprogram for determining compatibility

def compatibility(sign1, sign2):

    if sign1 == sign2:
        return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "rat":
        if sign2 == "dragon" or sign2 == "monkey" or sign2 == "ox":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "ox":
        if sign2 == "rat" or sign2 == "rooster" or sign2 == "snake":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "tiger":
        if sign2 == "horse" or sign2 == "dog" or sign2 == "pig":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "rabbit":
        if sign2 == "goat" or sign2 == "dog" or sign2 == "pig":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "dragon":
        if sign2 == "rat" or sign2 == "monkey" or sign2 == "rooster":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "snake":
        if sign2 == "ox" or sign2 == "rooster":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "horse":
        if sign2 == "tiger" or sign2 == "goat" or sign2 == "dog":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "goat":
        if sign2 == "rabbit" or sign2 == "horse" or sign2 == "pig":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "monkey":
        if sign2 == "rat" or sign2 == "dragon" or sign2 == "dog":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "rooster":
        if sign2 == "ox" or sign2 == "dragon" or sign2 == "snake":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "dog":
        if sign2 == "rabbit" or sign2 == "tiger" or sign2 == "horse" or sign2 == "monkey":
            return sign1 + " and " + sign2 + " are compatible."

    elif sign1 == "pig":
        if sign2 == "rabbit" or sign2 == "tiger" or sign2 == "goat":
            return sign1 + " and " + sign2 + " are compatible."


    return sign1 + " and " + sign2 + " are not compatible."


## Main - starting point of the program
# Get birthday

year, month, day = birthday()

print("Your birthday is ", year, month, day)

# Figure out sign1

sign1 = zodiac(year, month, day)

print("Your zodiac sign is:", sign1)

# Detect compatibility by finding out sign2

sign2 = input("Enter the zodiac sign you want to check compatibility with: ")

# Result of compatibility

result = compatibility(sign1, sign2)

print("The result is: " , result)







