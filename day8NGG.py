import random
from colorama import init, Fore

#Initialize Colorama
init(autoreset=True)

# Possible choices
choices = ["rock", "paper", "scissors"]

# Track wins
user_wins = 0
computer_wins = 0

print(Fore.YELLOW + "Welcome to Rock, Paper, Scissors!")
print("First to 3 wins! Let's go!\n")

while user_wins < 3 and computer_wins < 3:
    user_choice = input("Choose rock, paper, or scissors: \n").lower()
    if user_choice not in choices:
        print(Fore.RED + "Invalid choice. Try again. \n")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print (Fore.YELLOW + "It's a tie!\n")
    elif  (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(Fore.GREEN + "You win this round!\n")
        user_wins += 1
    else:
        print(Fore.red + "Sorry, Computer wins this round!\n")
        computer_wins += 1

    print(f"Score - You: {user_wins} | Computer: {computer_wins}\n")