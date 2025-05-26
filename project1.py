#Beginner level projects
#game 1
#Roll a dice game

import random
choice = input("Do you want to play the game(y/n):").lower()
playing = True


while playing:
   if choice == "y":
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      print(f"({die1},{die2})")
      break

   elif choice == "n":
      print("Thank you for playing the game!") 
      break
   else:
      print("Invalid choice.")
      break



#game 2 
#Number guessing game
import random

guess = random.randint(1,100)

while True:
    try:
       x = int(input("Guess a number between 1 to 100:"))

       if x > guess:
          print("Too high")
       elif x < guess:
          print("Too less")
       else:
          print("Yay! You guess it right")
    except ValueError:
       print("please enter a valid number:")
    

        


