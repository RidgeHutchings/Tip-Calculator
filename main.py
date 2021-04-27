# A simple tip split calculator

# ask the user how much their meal was
mealTotal = input("How much was your meal? ")

# ask how many members ate with the user
partySize = input("How many members in your party? ")

# ask what percentage of tip the user would like to leave
tipPercentage = input("What percentage of tip would you like to leave? ")

# convert user input into int() and float(). Display an error message if they entered incorrect data.

try:
    mealTotal = float(mealTotal)
except ValueError:
    print("invalid value entered. Please check your input and try again")

try:
    partySize = int(partySize)
except ValueError:
    print("invalid value entered. Please check your input and try again")
try:
    tipPercentage = float(tipPercentage) /100
except ValueError:
    print("invalid value entered. Please check your input and try again")

# perform calculation
perPersonTotal = (mealTotal * tipPercentage) / partySize


# display the perPersonTotal to the screen
print("Each person should pay $", round(perPersonTotal, 2))
