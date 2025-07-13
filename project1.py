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
    
#Game 3
#Rock, Paper, Scissors game 
import random
choices = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
   
#Game 4
#Hangman game
import random
def hangman():
    words = ["python", "java", "javascript", "hangman", "programming"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            return
    
    print(f"Game over! The word was: {word}")
hangman()
#Game 5
#Tic Tac Toe game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
      # Check rows, columns, and diagonals for a winner
      for row in board:
         if row[0] == row[1] == row[2] != " ":
               return row[0]
      for col in range(3):
         if board[0][col] == board[1][col] == board[2][col] != " ":
               return board[0][col]
      if board[0][0] == board[1][1] == board[2][2] != " ":
         return board[0][0]
      if board[0][2] == board[1][1] == board[2][0] != " ":
         return board[0][2]
      return None
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a tie!")
tic_tac_toe()
