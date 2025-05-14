#Beginner project
# #Guess the Number game

print("Welcome to the game")
print("Guess a  no. between 1 t0 10.")
x = int(input("Enter the number:"))
guess = 5
while True:
   if (guess == x):
      print("Yay! You have guess it right")
   else:
      print("Good luck next time")

return 0


