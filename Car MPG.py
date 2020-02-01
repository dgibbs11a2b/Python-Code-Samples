#----------------------------------------
#David Gibbs
#January 30, 2020
#
#This program takes the input in miles driven from a user,
#then it takes input value for the number of gallons of gas used
#and then calculates the car's miles per gallon rating and displays
#it to the screen

miles = float(input("How many miles did you drive on your last trip?: "))
# This line assigns miles as a floating point variable
gallons = int(input("How many gallons of gas did you use?: "))
# Thsi line assigns gallons as an integer variable
mpg = (miles / gallons)
# This line calculates the MPG
print ("Your car delivers", mpg, "miles per gallon of fuel.")
# This prints the car's MPG rating to the screen
