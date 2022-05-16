"""This simple Python Program collects user input
and computes retirement planning advice
Written by:
!!Richard Allan!!
for LU's CSIS 110 course
!!Summer 2021 B-03!!
Be sure you fully document your code with
comments like you see here."""


print("Hello,\n\n\tYou will need to press the Return key after \
replying to a request for information. Thank you.\n")

name = input("What is your name: ")
#This requests the user to input their name
cAge = input("How old are you (years only)?: ")
#This requests the user to give their age in years only, no months
cAge = int(cAge)
#this turns the input age into an integer
drAge = input("At what age would you like to retire (years only)?: ")
#This requests the user to give their age in years only, no months
drAge = int(drAge)
#Here the desired retirement age is made an integer
crSavings = input("How much do you currently have saved for retirement?:$ ")
#The user is now asked how much they have already saved
crSavings = float(crSavings)
#That savings is turned into an integer
arSavings = input("How much would you like to have saved by the time you retire?:$ ")
#The user is now able to input their desired retirement goal
arSavings = float(arSavings)
#That goal is now made an integer

ageDiff = (drAge - cAge)
savingsDiff = arSavings - crSavings
#These calculate the years until retirement and how much money needs to be saved

print("\nThank you,",name)
print("\nYou have", ageDiff, "years to save up for retirement.\n")

print('During these next', ageDiff, "years, you will need to save $", savingsDiff, "to reach your retirement goal.")
print('\nSpend wisely, save diligently, and God bless!')
#here the user is given the results of the calculations
