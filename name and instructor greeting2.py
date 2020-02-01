#----------------------------------------
#David Gibbs
#January 30, 2020
#
#This program requests input of my name
#and the first name of my instructor for the CSS225 class

username = input("Please enter your name: >> ")
#This line accepts input of a name to verify the following validated names

user1 = "David"
user2 = "Laleh"
#These are the only names that the program will accept and respond to

if username == user1:
    print("Hello", user1)
#Greets David only if David's name is assigned to user1 variable
elif username == user2:
    print("Hi there", user2)
#Greets Laleh only if Laleh's name is assigned to user2 variable
else:
    print("I'm sorry, I do not know you!")
#All other names are are not greeted
