# if-elif-else statements

import random
#a is a list
a = [50, 100, 200, 300]

# pick a random number from the list "a"
b = random.choice(a)

# the conditionals
if (b < 100):
    print("Number - " + str(a) + " is less than 100")
elif (b >= 100 and b < 200):
    print("Number - " + str(b) + " is greater than or equal to 100 but less than 200")
else:
    print("Number -" + str(b) + " is greater than or equal to 200")

# for me it prints
# Number - 100 is greater than or equal to 100 but less than 200
