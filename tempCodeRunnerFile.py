import random
choices = ["rock", "paper", "scissors"]
emojis = {'rock' : '🪨', 'paper' :'📜', 'scissor': '✂️'}
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {emojis[computer_choice]}")
    print(f"Your choice is {emojis[user_choice]}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")