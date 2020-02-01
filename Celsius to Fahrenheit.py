#----------------------------------------
#David Gibbs
#January 30, 2020
#
#This program requests input of the temperature in degrees in
#Fahrenheit and converts it into degrees in Celsius

Fahrenheit = float(input("Enter your temperature in Fahrenheit: "))
#This line requests the value in floating point format for Farenheit
Celsius = (Fahrenheit - 32) * 5.0 / 9.0
#This line converts from Celsius to Fahrenheit temperature 
print("The temperature of:", Fahrenheit, "Fahrenheit = ", Celsius, " C")
# This line displays the conversion results to the screen
