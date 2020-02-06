#----------------------------------------
#David Gibbs
#January 30, 2020
#
#This program requests input of my name
#and the first name of my instructor for the CSS225 class
#This is the correct version and return the expected result.  You did well!
username = input("Please enter your name: >> ")
#This line accepts input of a name to verify the following validated names
#You don't need to define two different variable names here.  Just one NAME would be sufficient.  See the sample code below:
#name = str(input("Please enter your name:"))
#if name == "Student1": # Add your name
#	print("Hello,",name,"!")
	
#elif name == "Laleh": #Add instuctor's name
#                print("Hello,",name,"!")
	
#else:
#	print("Name not recognized.")
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
