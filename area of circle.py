#----------------------------------------
#David Gibbs
#January 30, 2020
#
#This program takes the input from a user
#and finds the area of a circle using a value for radius squared

Pi = 3.14159265359
#This line defines Pi - the ratio of a circle's circumfrence 
radius = float(input('Enter the radius of the circle :'))
#Assigns the variable "radius" to the user's entry
area = Pi * radius ** 2
#Defines the formula to calculate the area of the circle using radius squared
print("Thank you for your entry, the area of the circle is:", (area))
#This line displays the calculated area to the screen
