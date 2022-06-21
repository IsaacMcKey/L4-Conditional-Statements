isHungry = input("Y/N: Are you hungry? ")
isBored = input("Y/N: Are you bored? ")

if(isHungry == "Y" or isHungry == "y"):
  print("Go eat")
else:
  print("Don't eat")
if(isBored == "Y"): 
  print("Go to sleep"or isBored == "y")
else:
  print ("Do nothing")

userNumber = int(input("Give me a number: "))
if(userNumber > 0):
  print("Your number is positive")
else:
  print("Your number is negative")
 
  # Ask the user for their age. 
  # If the user is older then 17, let them know that they can watch all movies 
  # If they're younger than 17 bnut older then 13, let them know that the y can watch G-Rated and PG-13
# If they're younger then 13,. they're o nly lalowed to watch just G-rated movies. 

userAge = int( input("Enter your age: "))

if(userAge >= 17): 
  print( "You can watch all movies!")
elif (userAge >= 13):
  print("You can watch G-rated and PG-13 movies!")
else: 
  print("You can only watch G-Rated movies.")

