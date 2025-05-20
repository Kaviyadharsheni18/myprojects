#Beginner level projects
# #Guess the Number game
#first

print("Welcome to the game")
print("Guess a  no. between 1 t0 100.")

guess = 12
playing = True
while playing:
    x = int(input('Enter a number between 1 to 100:'))
    if x < guess:
        print('Your guess is lesser than the answer')
        continue
     
    elif x > guess:
        print('Your guess is larger than the answer')
        continue
    elif x == guess:
        print('Yay You have guessed it right')
        break
    else:
        print('Invalid choice')

#second
#game 2
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

      
    

      
     
 

     
   

              
