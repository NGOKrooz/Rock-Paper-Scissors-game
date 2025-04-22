import random
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Possible choices
choices = ["rock", "paper", "scissors"]

def play_game():
    user_wins = 0
    computer_wins = 0

    print(Fore.YELLOW + "🎮 Welcome to Rock, Paper, Scissors Game!")
    print("First to 3 wins takes the crown! 👑\n")

    while user_wins < 3 and computer_wins < 3:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print(Fore.RED + "❌ Invalid choice. Try again. \n")
            continue

        computer_choice = random.choice(choices)
        print(f"\n 🖥️ Computer choice: {computer_choice}")

        if user_choice == computer_choice:
            print(Fore.YELLOW + "🤝 It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print(Fore.GREEN + "✅ You win this round! \n")
            user_wins += 1
        else:
            print(Fore.RED + "💻 Computer wins this round!\n")
            computer_wins += 1

        print(Fore.CYAN + f"Score - You: {user_wins} | Computer: {computer_wins}\n")

    # Winner Screen
    print("="*40)
    if user_wins == 3:
        print(Fore.GREEN + Style.BRIGHT + " 🏆Congratulations! You won the game! \n")
    else:
        print(Fore.RED + Style.BRIGHT + "😓 Oh no! The computer won this time. \n")

    print("="*40)  


    # Option to play again  
    
    play_again = input(Fore.YELLOW + "Love to play again? (yes or no): ").lower()
    if play_again == "yes":
        print("\n🔁 Restarting the game...\n")
        play_game()
    else:
        print(Fore.MAGENTA + "👋 Thanks for playing! Goodbye! \n")   

# Run the game
play_game()
